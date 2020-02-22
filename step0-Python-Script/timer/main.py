# -*- coding: UTF-8 -*-
import time

old_time = ''
flag = 1
def timer(interval):
    global flag
    global old_time
    if flag:
        old_time = time.strftime('%S', time.localtime(time.time()))
        flag = 0
    now_time = time.strftime('%S', time.localtime(time.time()))
    if int(old_time) >= 60-interval:
        if int(old_time)+interval-60 == int(now_time):
            print(time.strftime('%H:%M:%S', time.localtime(time.time())))
            old_time = now_time
    else:
        if int(now_time) - int(old_time) == interval:
            print(time.strftime('%H:%M:%S', time.localtime(time.time())))
            old_time = now_time

'''
Python 定时器：

输入间隔单位时间（单位s）
每到单位时间会执行一次函数，并显示当前时间
'''
if __name__ == "__main__":
    interval = int(input('请输入要间隔的时间：'))
    while True:
        timer(interval)
