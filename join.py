#!usr/bin/env python
# -*- coding:utf-8 -*-
import threading
from time import sleep
def f1():
    sleep(10)

t = threading.Thread(target=f1)
print("111")
t.start()
t.join(2)
print("222")