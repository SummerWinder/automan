# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import json, yaml
import Common.JsonTools as jsonTools
import Common.MysqlHandler as mysqlHandler
import KeyWordDriver.CommonKeyWord as ckw
from ApiLib.assistantapp import assistantappApi
from ApiLib.pet_auction import pet_auctionApi

def __defult(met, p, t):
    if p["header"].__len__() > 0:
        met.headers = p["header"]
    if p["parma"].__len__() > 0:
        met.params = p["parma"]
    if p["data"].__len__() > 0:
        met.data = p["data"]
    # if p["env"].__len__() > 0:
    #     met.changeEnv(p["env"])
    res = met.excute()
    if t == "text":
        return res.text
    if t == "dict":
        return json.loads(res.text)
    if t == "code":
        return res.status_code

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

def pet_auctionApi_UserLogin(p, t):
    met = pet_auctionApi.UserLogin()
    return __defult(met, p, t)


if __name__ == '__main__':
    pass