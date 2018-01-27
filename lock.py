#!usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time

gl_num = 0

lock = threading.RLock()

def show():
    lock.acquire()
    global gl_num
    time.sleep(1)
    gl_num += 1
    print(gl_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=show)
    t.start()

print("main thread stop")