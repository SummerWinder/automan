# -*- coding: utf-8 -*-
# @Time ：2020/8/14 1:35 PM
# @Author : Haoran
import os
import codecs,json
import configparser


proDir = os.path.dirname(__file__)
configPath = os.path.join(proDir, "../config.ini")

class readConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, dbName, name):
        value = self.cf.get(dbName, name)
        return value

if __name__ == '__main__':
    pass
    print(proDir)
    host = readConfig().get_db("DATABASE_TEST_cn_uniondrug_middleend_ordercenter","host")
    print(host)
    # tmp = '{"errno":0,"error":"请求成功","dataType":"OBJECT","data":{"skuNo":"53219-5062011","refNo":"5062011","waterNo":"2f16ee8ba21c4ea4a0e3bbcd4e8b2e7c","serviceDetails":null,"originPrice":null,"salePrice":1.00,"channel":8,"saleState":0,"goodsType":1,"goodsSubType":19,"title":"洋槐蜂蜜","subTitle":null,"isAgent":null,"totalAmount":null,"logoActivity":[],"highlights":[],"detailsImg":[],"packageIds":[],"packageExplainCos":null,"productServiceList":[{"name":"洋槐蜂蜜","price":null,"icon":null,"description":null,"skuNo":"53219-5062011"}],"memberId":null},"success":true,"fail":false}'

    # print(json.loads(tmp))