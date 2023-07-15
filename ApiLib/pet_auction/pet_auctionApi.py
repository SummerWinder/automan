# -*- coding: utf-8 -*-
from Common.HttpHandler import httpHandler


class UserLogin(httpHandler):
    def __init__(self):
        super(UserLogin, self).__init__()
        self.host = "https://pets.jckj928.cn/api/wanlshop/user/login"
        self.path = "/api/wanlshop/user/login"
        self.headers = {"Content-Type": "application/json;charset=UTF-8", 'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
                        'Content-type': 'multipart/form-data; boundary=wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'}
        self.params = None
        self.data = {"account": "18260682528", "password": "123456"}

    # def changeEnv(self, env):
    #     self.host = self.host.replace("turboradio.cn", env)

    def excute(self):
        if self.params != None:
            for k in self.params.keys():
                self.path = self.path + self.params[k]
        self.response = self.run(1)
        self.logger.info(self.path + "done" + "	账号密码登录")
        return self.response