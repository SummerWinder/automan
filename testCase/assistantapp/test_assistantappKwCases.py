# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw

import KeyWordDriver.BusinesskeyWord as bkw

class Test_assistantapp:

	@allure.feature("客户管理-查询客户")
	@allure.severity("blocker")
	def test_zjc_Customerinfo_001(self):
		# 读取yaml文件
		yamlFile = ckw.CommonKeyWord().Yaml_Read(r"D:\automan\TestFile\ZhangJunChao\zjctest.yaml")
		# 读取yaml里手机号
		mobile = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"mobileAssistant")
		# 读取Yaml执行环节
		env = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"env")
		# 登录发送验证码
		bkw.assistantappApi_CodeSend({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer"},"parma":{},"data":{"type":"login","mobile":mobile},"env":env},"dict")
		# 从数据库提取验证码-获取原始sql
		tmpSql = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"getLoginCaptcha")
		# 从数据库提取验证码-修改sql where条件
		finSql = ckw.CommonKeyWord().Str_Replace(tmpSql,18099990000,mobile)
		# 打印sql到控制台
		ckw.CommonKeyWord().Print_ToControl("sql:",finSql)
		# 打印sql到日志
		ckw.CommonKeyWord().Print_ToLog("sql:",finSql)
		# 从数据库提取验证码-执行查询
		sqlRes = ckw.CommonKeyWord().Db_MysqlSelect({"host":"udtest.uniondrug.com","port":"6033","username":"test","password":"tset@321abc","database":"cn_uniondrug_module_data","sql":finSql})
		# 打印查询结果到控制台
		ckw.CommonKeyWord().Print_ToControl("sql查询结果：",sqlRes)
		# 打印查询结果到日志
		ckw.CommonKeyWord().Print_ToLog("sql查询结果：",sqlRes)
		# 从数据库提取验证码-提取验证码01
		captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0],[["captcha"]])
		# 打印验证码到控制台
		ckw.CommonKeyWord().Print_ToControl("验证码：",captcha)
		# 打印验证码到日志
		ckw.CommonKeyWord().Print_ToLog("验证码：",captcha)
		# 登录获取token-调取接口
		loginRes = bkw.assistantappApi_UserSmsLogin({"header":{"Content-Type": "application/json;charsetUTF-8"},"parma":{},"data":{"mobile":mobile,"code":captcha},"env":env},"dict")
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","token"]])
		# 登录获取userid-提取userid
		userid = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","id"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 打印userid到控制台
		ckw.CommonKeyWord().Print_ToControl("userid：",userid)
		# 打印userid到日志
		ckw.CommonKeyWord().Print_ToLog("userid：",userid)
		# 客户管理列表页-调取接口
		CustomerPaging = bkw.assistantappApi_CustomerPaging({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":userid,"page":1,"limit":10},"env":env},"dict")
		# 提取客户列表errno
		CustomerPagingerrno = ckw.CommonKeyWord().Json_GetJsonValue(CustomerPaging,[["errno"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("Pagingerrno:",CustomerPagingerrno)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("Pagingerrno:",CustomerPagingerrno)
		# 读取yaml里客户列表断言
		CustomerPagingAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerPagingAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户列表断言结果：",CustomerPagingAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(CustomerPagingerrno,CustomerPagingAssert)
		# 客户管理详情页-调取接口
		CustomerInfo = bkw.assistantappApi_CustomerInfo({"header":{"Content-Type": "application/json;charsetUTF-8","Authorization":"Bearer "+token},"parma":{},"data":{"userId":userid,"customerId": "7159"},"env":env},"dict")
		# 提取客户详情contacts
		contacts = ckw.CommonKeyWord().Json_GetJsonValue(CustomerInfo,[["data","contacts"]])
		# 打印结果到控制台
		ckw.CommonKeyWord().Print_ToControl("contacts:",contacts)
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("contacts:",contacts)
		# 读取yaml里客户详情断言
		CustomerInfoAssert = ckw.CommonKeyWord().Yaml_GetByKey(yamlFile,"CustomerInfoAssert")
		# 打印结果到日志
		ckw.CommonKeyWord().Print_ToLog("客户详情断言结果：",CustomerInfoAssert)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(contacts,CustomerInfoAssert)
		# 强制等待
		ckw.CommonKeyWord().Time_Sleep("1.0")
