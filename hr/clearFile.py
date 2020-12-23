import os
import threading
import time
from queue import Queue


class myThread1(threading.Thread):  # 继承父类threading.Thread
    wait_delete_staff_icon_queue = Queue(maxsize=0)
    prefix = os.getcwd()

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        while True:
            if self.wait_delete_staff_icon_queue.qsize() > 0:
                delete_file = self.prefix + self.wait_delete_staff_icon_queue.get().replace("/", "\\")
                # print("待删除头像名称队列大小：" + str(self.wait_delete_staff_icon_queue.qsize()))
                # print("待删除文件名称：" + delete_file)
                # print(os.path.exists(delete_file))
                if os.path.exists(delete_file):
                    os.remove(delete_file)
                    print("删除用户头像:" + delete_file)
            time.sleep(10)


# tt = "/media/uploads/2020/12/23/1233_bw9cRRj.jpg"
# print(tt.replace("/", "\\"))

