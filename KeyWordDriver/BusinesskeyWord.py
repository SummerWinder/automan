# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import json, yaml
import Common.JsonTools as jsonTools
import Common.MysqlHandler as mysqlHandler
import KeyWordDriver.CommonKeyWord as ckw
import ApiLib.goodsCenter.goodsCenterApi as goodCenter
import ApiLib.orderCenter.orderCenterApi as orderCenter
import ApiLib.equityCenter.equityCenterApi as equityCenter
import ApiLib.auth.authApi as auth
import ApiLib.thePublic.thePublicApi as thePublicApi
from ApiLib.customerCenter import customerCenterApi
from ApiLib.drugapp import drugappApi
from ApiLib.equityCenter import equityCenterApi
from ApiLib.goodsCenter import goodsCenterApi
from ApiLib.orderCenter import orderCenterApi
from ApiLib.promoteCenter import promoteCenterApi
from ApiLib.recommend import recommendApi
from ApiLib.searchCenter import searchCenterApi
from ApiLib.tag import tagApi
from ApiLib.unifyorder import unifyorderApi
from ApiLib.userCenter import userCenterApi
from ApiLib.backendApp import backendApi
from ApiLib.creditCenter import creditCenterApi
from ApiLib.assistantapp import assistantappApi


def goodCenterApi_SpuQuery(p, t):
    met = goodCenter.spuQuery()
    return __defult(met, p, t)


def goodCenterApi_UnifyproductDetails(p, t):
    met = goodCenter.UnifyproductDetails()
    return __defult(met, p, t)


def goodCenterApi_UnifyproductBuyLimit(p, t):
    met = goodCenter.UnifyproductBuyLimit()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderConfirmCreate(p, t):
    met = orderCenter.UnifyorderConfirmCreate()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderConfirmInvoiceChange(p, t):
    met = orderCenter.UnifyorderConfirmInvoiceChange()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderOrderCreate(p, t):
    met = orderCenter.UnifyorderOrderCreate()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierPayModes(p, t):
    met = orderCenter.UnifyorderCashierPayModes()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderOrderDetail(p, t):
    met = orderCenter.UnifyorderOrderDetail()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierCheck(p, t):
    met = orderCenter.UnifyorderCashierCheck()
    return __defult(met, p, t)


def orderCenterApi_UnifyorderCashierCreate(p, t):
    met = orderCenter.UnifyorderCashierCreate()
    return __defult(met, p, t)


def equityCenterApi_UnifyorderMemberEquityQuery(p, t):
    met = equityCenter.UnifyorderMemberEquityQuery()
    return __defult(met, p, t)


def equityCenterApi_UnifyorderConfirmEquityChange(p, t):
    met = equityCenter.UnifyorderConfirmEquityChange()
    return __defult(met, p, t)


def equityCenterApi_RedeemAdd(p, t):
    met = equityCenter.RedeemAdd()
    return __defult(met, p, t)


def authApi_LoginSendCaptcha(p, t):
    met = auth.LoginSendCaptcha()
    return __defult(met, p, t)


def authApi_SmsSend(p, t):
    met = auth.SmsSend()
    return __defult(met, p, t)


def authApi_DdMobilelogin(p, t):
    met = auth.DdMobilelogin()
    return __defult(met, p, t)


def authApi_Ddlogin(p, t):
    met = auth.Ddlogin()
    return __defult(met, p, t)


def authApi_ThePublicLoginSendCaptcha(p, t):
    met = auth.ThePublicLoginSendCaptcha()
    return __defult(met, p, t)


def authApi_ThePublicLoginLogin(p, t):
    met = auth.ThePublicLoginLogin()
    return __defult(met, p, t)


def authApi_GetCaptcha(p):
    db = mysqlHandler.mysqlHandler(p["dbName"])
    f = open("/Users/liuhaoran/PycharmProjects/automan/TestFile/HaoRanOnly/lhrtest.yaml", "r", encoding="utf-8")
    tmp = yaml.load(f.read())
    f.close()
    oo = tmp["getLoginCaptcha"].replace("15005150023", p["mobile"])
    print(oo)
    db.sql = oo
    ww = db.excute().fetchall()
    print(ww[0][0])
    print(type(ww[0][0]))
    qq = ckw.CommonKeyWord().json_GetJsonValue(json.loads(ww[0][0]), [["sms", "code"]])
    print(qq)
    return qq


def authApi_LoginLogin(p, t):
    met = auth.LoginLogin()
    return __defult(met, p, t)


def thePublicApi_ThePublicLoginSendCaptcha(p, t):
    met = thePublicApi.ThePublicLoginSendCaptcha()
    return __defult(met, p, t)


def thePublicApi_ThePublicLoginLogin(p, t):
    met = thePublicApi.ThePublicLoginLogin()
    return __defult(met, p, t)


def thePublicApi_VMemberDetail(p, t):
    met = thePublicApi.VMemberDetail()
    return __defult(met, p, t)


def thePublicApi_VProjectUserCheck(p, t):
    met = thePublicApi.VProjectUserCheck()
    return __defult(met, p, t)


def thePublicApi_VProjectUserDetail(p, t):
    met = thePublicApi.VProjectUserDetail()
    return __defult(met, p, t)


def thePublicApi_VEquityNewActivate(p, t):
    met = thePublicApi.VEquityNewActivate()
    return __defult(met, p, t)


def thePublicApi_VWxUserinfo(p, t):
    met = thePublicApi.VEquityNewActivate()
    return __defult(met, p, t)


'''
haoran统一交易根据权益卡id提取信息
勿动    1000690099471315
'''


def getRsourceInfo_byCardNo(l, cardNo):
    for card in l:
        print(jsonTools.getJsonValue(card, [["rsourceId"]]), cardNo)
        if jsonTools.getJsonValue(card, [["rsourceId"]]) == str(cardNo):
            return card
    return None


def thePublicApi_ExtTemplateOperate(p, t):
    met = thePublicApi.ExtTemplateOperate()
    return __defult(met, p, t)


def thePublicApi_VProjectUserCondition(p, t):
    met = thePublicApi.VProjectUserCondition()
    return __defult(met, p, t)


def thePublicApi_VProjectUserGroup(p, t):
    met = thePublicApi.VProjectUserGroup()
    return __defult(met, p, t)


def equityCenter_RedeemDisable(p, t):
    met = equityCenter.RedeemDisable()
    return __defult(met, p, t)


def __defult(met, p, t):
    if p["header"].__len__() > 0:
        met.headers = p["header"]
    if p["parma"].__len__() > 0:
        met.params = p["parma"]
    if p["data"].__len__() > 0:
        met.data = p["data"]
    if p["env"].__len__() > 0:
        met.changeEnv(p["env"])
    res = met.excute()
    if t == "text":
        return res.text
    if t == "dict":
        return json.loads(res.text)
    if t == "code":
        return res.status_code


if __name__ == '__main__':
    pass


def customerCenterApi_PromoteSendcard(p, t):
    met = customerCenterApi.PromoteSendcard()
    return __defult(met, p, t)


def customerCenterApi_VoucherCreate(p, t):
    met = customerCenterApi.VoucherCreate()
    return __defult(met, p, t)


def drugappApi_AssistantCreate(p, t):
    met = drugappApi.AssistantCreate()
    return __defult(met, p, t)


def drugappApi_V4CodePicture(p, t):
    met = drugappApi.V4CodePicture()
    return __defult(met, p, t)


def drugappApi_V4CodeVerify(p, t):
    met = drugappApi.V4CodeVerify()
    return __defult(met, p, t)


def drugappApi_V4UsersSmslogin(p, t):
    met = drugappApi.V4UsersSmslogin()
    return __defult(met, p, t)


def equityCenterApi_RedeemDisable(p, t):
    met = equityCenterApi.RedeemDisable()
    return __defult(met, p, t)


def goodsCenterApi_SpuQuery(p, t):
    met = goodsCenterApi.SpuQuery()
    return __defult(met, p, t)


def goodsCenterApi_UnifyproductDetails(p, t):
    met = goodsCenterApi.UnifyproductDetails()
    return __defult(met, p, t)


def goodsCenterApi_UnifyproductBuyLimit(p, t):
    met = goodsCenterApi.UnifyproductBuyLimit()
    return __defult(met, p, t)


def orderCenterApi_paging(p, t):
    met = orderCenterApi.paging()
    return __defult(met, p, t)


def orderCenterApi_NeworderOrdercancelsub(p, t):
    met = orderCenterApi.NeworderOrdercancelsub()
    return __defult(met, p, t)


def recommendApi_AdvisorListRecommendAdv(p, t):
    met = recommendApi.AdvisorListRecommendAdv()
    return __defult(met, p, t)


def searchCenterApi_WordSuggesterSuggester(p, t):
    met = searchCenterApi.WordSuggesterSuggester()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsAll(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsAll()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsByTradeCode(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsByTradeCode()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchGoodsGeo(p, t):
    met = searchCenterApi.GoodsSearchSearchGoodsGeo()
    return __defult(met, p, t)


def searchCenterApi_OtoManageSearch(p, t):
    met = searchCenterApi.OtoManageSearch()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchCorrectSearchContent(p, t):
    met = searchCenterApi.GoodsSearchCorrectSearchContent()
    return __defult(met, p, t)


def searchCenterApi_QueryGoodsQueryGoodsBaseInfo(p, t):
    met = searchCenterApi.QueryGoodsQueryGoodsBaseInfo()
    return __defult(met, p, t)


def searchCenterApi_SkuQuery(p, t):
    met = searchCenterApi.SkuQuery()
    return __defult(met, p, t)


def searchCenterApi_Sku(p, t):
    met = searchCenterApi.Sku()
    return __defult(met, p, t)


def searchCenterApi_SkuSimple(p, t):
    met = searchCenterApi.SkuSimple()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchUnify(p, t):
    met = searchCenterApi.GoodsSearchSearchUnify()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearch(p, t):
    met = searchCenterApi.GoodsSearchSearch()
    return __defult(met, p, t)


def searchCenterApi_GoodsSearchSearchDtpGoods(p, t):
    met = searchCenterApi.GoodsSearchSearchDtpGoods()
    return __defult(met, p, t)


def tagApi_UserPackageBaseCreate(p, t):
    met = tagApi.UserPackageBaseCreate()
    return __defult(met, p, t)


def tagApi_UserPackageHighlevelCreate(p, t):
    met = tagApi.UserPackageHighlevelCreate()
    return __defult(met, p, t)


def tagApi_UserPackageUsersGet(p, t):
    met = tagApi.UserPackageUsersGet()
    return __defult(met, p, t)


def tagApi_MemberWideInsertMemberPackage(p, t):
    met = tagApi.MemberWideInsertMemberPackage()
    return __defult(met, p, t)


def tagApi_OrderWideInsertOrderPackage(p, t):
    met = tagApi.OrderWideInsertOrderPackage()
    return __defult(met, p, t)


def tagApi_UserPackageDelete(p, t):
    met = tagApi.UserPackageDelete()
    return __defult(met, p, t)


def tagApi_UserPackageListMember(p, t):
    met = tagApi.UserPackageListMember()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmCreate(p, t):
    met = unifyorderApi.UnifyorderConfirmCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmInvoiceChange(p, t):
    met = unifyorderApi.UnifyorderConfirmInvoiceChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderOrderCreate(p, t):
    met = unifyorderApi.UnifyorderOrderCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierPayModes(p, t):
    met = unifyorderApi.UnifyorderCashierPayModes()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderOrderDetail(p, t):
    met = unifyorderApi.UnifyorderOrderDetail()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierCheck(p, t):
    met = unifyorderApi.UnifyorderCashierCheck()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderCashierCreate(p, t):
    met = unifyorderApi.UnifyorderCashierCreate()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberEquityQuery(p, t):
    met = unifyorderApi.UnifyorderMemberEquityQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmEquityChange(p, t):
    met = unifyorderApi.UnifyorderConfirmEquityChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberIntegralUse(p, t):
    met = unifyorderApi.UnifyorderMemberIntegralUse()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberIntegralStop(p, t):
    met = unifyorderApi.UnifyorderMemberIntegralStop()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberResourceQuery(p, t):
    met = unifyorderApi.UnifyorderMemberResourceQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmResouceChange(p, t):
    met = unifyorderApi.UnifyorderConfirmResouceChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyproductDetails(p, t):
    met = unifyorderApi.UnifyproductDetails()
    return __defult(met, p, t)


def unifyorderApi_UnifyproductBuyLimit(p, t):
    met = unifyorderApi.UnifyproductBuyLimit()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmRemark(p, t):
    met = unifyorderApi.UnifyorderConfirmRemark()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderAddressQueryInfos(p, t):
    met = unifyorderApi.UnifyorderAddressQueryInfos()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmShipmentChange(p, t):
    met = unifyorderApi.UnifyorderConfirmShipmentChange()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderAddressAdd(p, t):
    met = unifyorderApi.UnifyorderAddressAdd()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderMemberCouponQuery(p, t):
    met = unifyorderApi.UnifyorderMemberCouponQuery()
    return __defult(met, p, t)


def unifyorderApi_UnifyorderConfirmCouponChange(p, t):
    met = unifyorderApi.UnifyorderConfirmCouponChange()
    return __defult(met, p, t)


def customerCenterApi_VoucherListing(p, t):
    met = customerCenterApi.VoucherListing()
    return __defult(met, p, t)


def customerCenterApi_PromoteCardlist(p, t):
    met = customerCenterApi.PromoteCardlist()
    return __defult(met, p, t)


def userCenterApi_MngUserUserSave(p, t):
    met = userCenterApi.MngUserUserSave()
    return __defult(met, p, t)


def userCenterApi_MngUserUserUpdate(p, t):
    met = userCenterApi.MngUserUserUpdate()
    return __defult(met, p, t)


def userCenterApi_MngUserUserUpdateStatus(p, t):
    met = userCenterApi.MngUserUserUpdateStatus()
    return __defult(met, p, t)


def userCenterApi_V2ApiUserCardAdd(p, t):
    met = userCenterApi.V2ApiUserCardAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardApproveSetStatus(p, t):
    met = userCenterApi.MngUserUserCardApproveSetStatus()
    return __defult(met, p, t)


def userCenterApi_MngUserUserPage(p, t):
    met = userCenterApi.MngUserUserPage()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagAdd(p, t):
    met = userCenterApi.MngUserUserTagAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagDetail(p, t):
    met = userCenterApi.MngUserUserTagDetail()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagGet(p, t):
    met = userCenterApi.MngUserUserTagGet()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgAdd(p, t):
    met = userCenterApi.V2ApiOrgAdd()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgQueryBy(p, t):
    met = userCenterApi.V2ApiOrgQueryBy()
    return __defult(met, p, t)


def userCenterApi_V2ApiOrgRemove(p, t):
    met = userCenterApi.V2ApiOrgRemove()
    return __defult(met, p, t)


def userCenterApi_MngUserUserTagRemove(p, t):
    met = userCenterApi.MngUserUserTagRemove()
    return __defult(met, p, t)


def userCenterApi_MngUserUserIdentityUpdate(p, t):
    met = userCenterApi.MngUserUserIdentityUpdate()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardAdd(p, t):
    met = userCenterApi.MngUserUserCardAdd()
    return __defult(met, p, t)


def userCenterApi_MngUserUserCardUpdate(p, t):
    met = userCenterApi.MngUserUserCardUpdate()
    return __defult(met, p, t)


def userCenterApi_V2ApiUserCardAddByNo(p, t):
    met = userCenterApi.V2ApiUserCardAddByNo()
    return __defult(met, p, t)


def orderCenterApi_OrderCacheDel(p, t):
    met = orderCenterApi.OrderCacheDel()
    return __defult(met, p, t)


def orderCenterApi_LogisticsDeliverNotify(p, t):
    met = orderCenterApi.LogisticsDeliverNotify()
    return __defult(met, p, t)


def orderCenterApi_NeworderRefundcashier(p, t):
    met = orderCenterApi.NeworderRefundcashier()
    return __defult(met, p, t)


def promoteCenterApi_PromoteSchemeAdd(p, t):
    met = promoteCenterApi.PromoteSchemeAdd()
    return __defult(met, p, t)


def promoteCenterApi_PromoteSendcard(p, t):
    met = promoteCenterApi.PromoteSendcard()
    return __defult(met, p, t)


def adminBackend_login(mobile, env):
    # 登录药联后台
    authApi_SmsSend(
        {"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {}, "data": {"mobile": mobile},
         "env": env}, "dict")
    # 从数据库提取验证码-获取原始sql
    tmpSql = "SELECT captcha FROM `cn_uniondrug_module_data`.`captcha` where mobile = '15005150023' ORDER BY id desc LIMIT 1"
    # 从数据库提取验证码-修改sql where条件
    finSql = ckw.CommonKeyWord().Str_Replace(tmpSql, 15005150023, mobile)
    # 从数据库提取验证码-执行查询
    sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", finSql)

    code = ckw.jsonTools.getJsonValue(sqlRes[0], [["captcha"]])
    reslogin = authApi_DdMobilelogin({"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {},
                                      "data": {"mobile": mobile, "code": code}, "env": env}, "dict")
    tmp = ckw.CommonKeyWord().Json_GetJsonValue(reslogin, [["data"]])
    tmpToken = ckw.CommonKeyWord().Json_GetJsonValue(tmp, [["token"]])
    bb = authApi_Ddlogin(
        {"header": {"Content-Type": "application/json;charset=UTF-8"}, "parma": {}, "data": {"token": tmpToken},
         "env": env}, "dict")
    backToken = ckw.jsonTools.getJsonValue(bb, [["data", "token"]])
    return backToken


def thePublic_login(mobile, env):
    # 登录发送验证码
    authApi_LoginSendCaptcha(
        {"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {}, "data": {"mobile": mobile},
         "env": env}, "dict")
    # 从数据库提取验证码-获取原始sql
    tmpSql = "SELECT * FROM `cn_uniondrug_module_sms`.`message` WHERE mobile = '15005150023' ORDER BY gmtCreated DESC LIMIT 1;"
    # 从数据库提取验证码-修改sql where条件
    finSql = ckw.CommonKeyWord().Str_Replace(tmpSql, 15005150023, mobile)
    # 从数据库提取验证码-执行查询
    sqlRes = ckw.CommonKeyWord().Db_ConfMysqlSelect("DATABASE_TEST_ALL", finSql)
    # 打印查询结果到控制台
    ckw.CommonKeyWord().Print_ToControl("sql查询结果：", sqlRes)
    # 打印查询结果到日志
    ckw.CommonKeyWord().Print_ToLog("sql查询结果：", sqlRes)
    # 从数据库提取验证码-提取验证码01
    captcha = ckw.CommonKeyWord().Json_GetJsonValue(sqlRes[0], [["data"]])
    # 从数据库提取验证码-提取验证码02
    captcha = ckw.CommonKeyWord().Json_GetJsonValue(captcha, [["sms", "code"]])
    # 打印验证码到控制台
    ckw.CommonKeyWord().Print_ToControl("验证码：", captcha)
    # 打印验证码到日志
    ckw.CommonKeyWord().Print_ToLog("验证码：", captcha)
    # 登录获取token-调取接口
    loginRes = authApi_LoginLogin({"header": {"Content-Type": "application/json;charsetUTF-8"}, "parma": {},
                                   "data": {"mobile": mobile, "code": captcha}, "env": env}, "dict")
    token = ckw.CommonKeyWord().Json_GetJsonValue(loginRes, [["data", "token"]])
    return token


def authApi_RegisterGs(p, t):
    met = auth.RegisterGs()
    return __defult(met, p, t)


def backendApi_OrdersCart(p, t):
    met = backendApi.OrdersCart()
    return __defult(met, p, t)


def backendApi_DtpOrdersCart(p, t):
    met = backendApi.DtpOrdersCart()
    return __defult(met, p, t)


def backendApi_MerhantVillageDoctor(p, t):
    met = backendApi.MerhantVillageDoctor()
    return __defult(met, p, t)


def backendApi_VillageDoctorOrdersCart(p, t):
    met = backendApi.VillageDoctorOrdersCart()
    return __defult(met, p, t)


def backendApi_Recipe(p, t):
    met = backendApi.Recipe()
    return __defult(met, p, t)


def backendApi_RecipeCart(p, t):
    met = backendApi.RecipeCart()
    return __defult(met, p, t)


def backendApi_RenewCart(p, t):
    met = backendApi.RenewCart()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngPaging(p, t):
    met = orderCenterApi.MngOrderOrderMngPaging()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngDetail(p, t):
    met = orderCenterApi.MngOrderOrderMngDetail()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngOrderallequity(p, t):
    met = orderCenterApi.MngOrderOrderMngOrderallequity()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngExpresslist(p, t):
    met = orderCenterApi.MngOrderOrderMngExpresslist()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngOrdercancelsub(p, t):
    met = orderCenterApi.MngOrderOrderMngOrdercancelsub()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundlist(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundlist()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngDeliver(p, t):
    met = orderCenterApi.MngOrderOrderMngDeliver()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundgoods(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundgoods()
    return __defult(met, p, t)


def orderCenterApi_MngOrderOrderMngRefundcashier(p, t):
    met = orderCenterApi.MngOrderOrderMngRefundcashier()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountTradeAdd(p, t):
    met = creditCenterApi.CreditAccountTradeAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountTradeBatchAdd(p, t):
    met = creditCenterApi.CreditAccountTradeBatchAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditGoodsTradeTransfer(p, t):
    met = creditCenterApi.CreditGoodsTradeTransfer()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeTrialCalculation(p, t):
    met = creditCenterApi.CreditPayTradeTrialCalculation()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeLock(p, t):
    met = creditCenterApi.CreditPayTradeLock()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeRelease(p, t):
    met = creditCenterApi.CreditPayTradeRelease()
    return __defult(met, p, t)


def creditCenterApi_CreditPayTradeConsume(p, t):
    met = creditCenterApi.CreditPayTradeConsume()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradePreAdd(p, t):
    met = creditCenterApi.CreditPreAccountTradePreAdd()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEdit(p, t):
    met = creditCenterApi.CreditPreAccountTradeEdit()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEditBatch(p, t):
    met = creditCenterApi.CreditPreAccountTradeEditBatch()
    return __defult(met, p, t)


def creditCenterApi_CreditIntegralTradeWithdraw(p, t):
    met = creditCenterApi.CreditIntegralTradeWithdraw()
    return __defult(met, p, t)


def creditCenterApi_CreditIntegralTradeConfirmWithdraw(p, t):
    met = creditCenterApi.CreditIntegralTradeConfirmWithdraw()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeCheckCompanyCredit(p, t):
    met = creditCenterApi.CreditCompanySettleTradeCheckCompanyCredit()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradePullCompanyRecords(p, t):
    met = creditCenterApi.CreditCompanySettleTradePullCompanyRecords()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeSettleApply(p, t):
    met = creditCenterApi.CreditCompanySettleTradeSettleApply()
    return __defult(met, p, t)


def creditCenterApi_CreditCompanySettleTradeSettleConfirm(p, t):
    met = creditCenterApi.CreditCompanySettleTradeSettleConfirm()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryPreCount(p, t):
    met = creditCenterApi.CreditAccountQueryPreCount()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryCountHistory(p, t):
    met = creditCenterApi.CreditAccountQueryCountHistory()
    return __defult(met, p, t)


def creditCenterApi_CreditPreAccountTradeEditInfo(p, t):
    met = creditCenterApi.CreditPreAccountTradeEditInfo()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountAdminExport(p, t):
    met = creditCenterApi.CreditAccountAdminExport()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryMemberAccountQuery(p, t):
    met = creditCenterApi.CreditAccountQueryMemberAccountQuery()
    return __defult(met, p, t)


def creditCenterApi_CreditAccountQueryPrePaging(p, t):
    met = creditCenterApi.CreditAccountQueryPrePaging()
    return __defult(met, p, t)


def assistantappApi_UserLogin(p, t):
    met = assistantappApi.UserLogin()
    return __defult(met, p, t)


def assistantappApi_CodeSend(p, t):
    met = assistantappApi.CodeSend()
    return __defult(met, p, t)


def assistantappApi_UserSmsLogin(p, t):
    met = assistantappApi.UserSmsLogin()
    return __defult(met, p, t)


def assistantappApi_CustomerAdd(p, t):
    met = assistantappApi.CustomerAdd()
    return __defult(met, p, t)


def assistantappApi_CustomerPaging(p, t):
    met = assistantappApi.CustomerPaging()
    return __defult(met, p, t)


def assistantappApi_CustomerInfo(p, t):
    met = assistantappApi.CustomerInfo()
    return __defult(met, p, t)


def assistantappApi_CustomerEdit(p, t):
    met = assistantappApi.CustomerEdit()
    return __defult(met, p, t)


def assistantappApi_CustomerDelete(p, t):
    met = assistantappApi.CustomerDelete()
    return __defult(met, p, t)


def assistantappApi_InspectCreate(p, t):
    met = assistantappApi.InspectCreate()
    return __defult(met, p, t)


def assistantappApi_VisitAddCommonVisit(p, t):
    met = assistantappApi.VisitAddCommonVisit()
    return __defult(met, p, t)


def assistantappApi_VisitArrivalVisit(p, t):
    met = assistantappApi.VisitArrivalVisit()
    return __defult(met, p, t)


def assistantappApi_VisitVisitComplete(p, t):
    met = assistantappApi.VisitVisitComplete()
    return __defult(met, p, t)


def assistantappApi_VisitAddInterimVisit(p, t):
    met = assistantappApi.VisitAddInterimVisit()
    return __defult(met, p, t)


def assistantappApi_VisitPaging(p, t):
    met = assistantappApi.VisitPaging()
    return __defult(met, p, t)


def assistantappApi_VisitInfo(p, t):
    met = assistantappApi.VisitInfo()
    return __defult(met, p, t)


def assistantappApi_InspectStart(p, t):
    met = assistantappApi.InspectStart()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreUpdate(p, t):
    met = assistantappApi.MerchantStoreUpdate()
    return __defult(met, p, t)


def assistantappApi_InspectUpdate(p, t):
    met = assistantappApi.InspectUpdate()
    return __defult(met, p, t)


def assistantappApi_InspectList(p, t):
    met = assistantappApi.InspectList()
    return __defult(met, p, t)


def assistantappApi_InspectDetail(p, t):
    met = assistantappApi.InspectDetail()
    return __defult(met, p, t)


def assistantappApi_MerchantList(p, t):
    met = assistantappApi.MerchantList()
    return __defult(met, p, t)


def assistantappApi_MerchantInfo(p, t):
    met = assistantappApi.MerchantInfo()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreList(p, t):
    met = assistantappApi.MerchantStoreList()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreDetail(p, t):
    met = assistantappApi.MerchantStoreDetail()
    return __defult(met, p, t)


def assistantappApi_AssistantRegister(p, t):
    met = assistantappApi.AssistantRegister()
    return __defult(met, p, t)


def assistantappApi_V4CodeSend(p, t):
    met = assistantappApi.V4CodeSend()
    return __defult(met, p, t)


def assistantappApi_MerchantStoreIsCanAdd(p, t):
    met = assistantappApi.MerchantStoreIsCanAdd()
    return __defult(met, p, t)


def assistantappApi_MerchantStorePush(p, t):
    met = assistantappApi.MerchantStorePush()
    return __defult(met, p, t)


def assistantappApi_AssistantLists(p, t):
    met = assistantappApi.AssistantLists()
    return __defult(met, p, t)


def assistantappApi_AssistantDetail(p, t):
    met = assistantappApi.AssistantDetail()
    return __defult(met, p, t)


def assistantappApi_AssistantStoreTransfer(p, t):
    met = assistantappApi.AssistantStoreTransfer()
    return __defult(met, p, t)


def assistantappApi_AssistantUpdate(p, t):
    met = assistantappApi.AssistantUpdate()
    return __defult(met, p, t)

def assistantappApi_WorkList(p, t):
    met = assistantappApi.WorkList()
    return __defult(met, p, t)

def assistantappApi_WorkJob(p, t):
    met = assistantappApi.WorkJob()
    return __defult(met, p, t)

def userCenterApi_UserBasicQuery(p, t):
	met = userCenterApi.UserBasicQuery()
	return __defult(met, p, t)
def userCenterApi_MngTaskUpdate(p, t):
	met = userCenterApi.MngTaskUpdate()
	return __defult(met, p, t)
def imApi_MyCustomers(p, t):
	met = imApi.MyCustomers()
	return __defult(met, p, t)
def imApi_GetRecommendAdvisor1(p, t):
	met = imApi.GetRecommendAdvisor1()
	return __defult(met, p, t)
def imApi_GetRecommendAdvisor2(p, t):
	met = imApi.GetRecommendAdvisor2()
	return __defult(met, p, t)
def imApi_GetAdvisorInfo(p, t):
	met = imApi.GetAdvisorInfo()
	return __defult(met, p, t)
def imApi_GetBindAdvisorInfo(p, t):
	met = imApi.GetBindAdvisorInfo()
	return __defult(met, p, t)
def stagnationApi_StagnationUserStatistic(p, t):
	met = stagnationApi.StagnationUserStatistic()
	return __defult(met, p, t)
def stagnationApi_StagnationUserRecordPaging(p, t):
	met = stagnationApi.StagnationUserRecordPaging()
	return __defult(met, p, t)
def assistantappApi_WorkCancel(p, t):
	met = assistantappApi.WorkCancel()
	return __defult(met, p, t)
def assistantappApi_WorkAccept(p, t):
	met = assistantappApi.WorkAccept()
	return __defult(met, p, t)
def assistantappApi_WorkRecordCreate(p, t):
	met = assistantappApi.WorkRecordCreate()
	return __defult(met, p, t)
def assistantappApi_WorkRecordComplete(p, t):
	met = assistantappApi.WorkRecordComplete()
	return __defult(met, p, t)