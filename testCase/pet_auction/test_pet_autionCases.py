# -*- coding: utf-8 -*-
import pytest,os,allure
import KeyWordDriver.CommonKeyWord as ckw
import KeyWordDriver.BusinesskeyWord as bkw

class Test_pet_auction:

	@allure.feature("账号密码登录")
	@allure.severity("blocker")
	def test_UserLogin(self):
		# 登录获取token-调取接口
		loginRes = bkw.pet_auctionApi_UserLogin({"header":{"Content-Type": "application/json", 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)'},
												 "parma":{},
                                                 "data":{"account": "u_lP9hcK", "password": "123456"}},"dict")
		# 登录获取errno
		errno = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["code"]])
		# 登录获取token-提取token
		token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes,[["data","userinfo","token"]])
		# 打印token到控制台
		ckw.CommonKeyWord().Print_ToControl("token：",token)
		# 打印token到日志
		ckw.CommonKeyWord().Print_ToLog("token：",token)
		# 断言对比字典
		assert ckw.CommonKeyWord().Assert_ObjAndObj(errno,1)
