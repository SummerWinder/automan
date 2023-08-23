import time, threading_study
from datetime import datetime


class OnLoadFinish:
    def __init__(self):
        self.is_finished = False
    def on_load_finish(self):
        time.sleep(5)
        self.is_finished = True

    def position(self):
        position_original = ['bu2401', '1',  '2', '3', '4', 'bu2401', '2',  '2', '3', '4']
        position_list = []
        real_position = {}
        # 把合约数据写入字典，定义好key值
        real_position["Instrument"] = position_original[0]
        real_position["position"] = position_original[1]
        real_position["yesterday_position"] = position_original[2]
        real_position["today_position"] = position_original[3]
        real_position["available_position"] = position_original[4]
        # 合约数据存入列表中
        position_list.append(real_position)
        # print(real_position)
        print(position_list)

    def scheduled_task(self):
        onload = OnLoadFinish().position()
        t = threading.Timer(10, onload)
        t.start()


if __name__ == "__main__":
    onload = OnLoadFinish()
    # onload.wait()
    # onload.position()
    onload.scheduled_task()