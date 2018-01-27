#!usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import time

def f1(a1):
    time.sleep(2)
    print(a1)

if __name__ == "__main__":
    t = multiprocessing.Process(target=f1, args=(11,))
    t.daemon = True
    t.start()
    t2 = multiprocessing.Process(target=f1, args=(22,))
    t2.daemon = True
    t2.start()
    print("end")