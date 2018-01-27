#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process,Pool
import time

def Foo(i):
    time.sleep(2)
    print(i+100)

def Bar(arg):
    print(arg)



if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply(func=Foo, args=(i,))
        pool.apply_async(func=Foo, args=(i,))
    pool.close()
    pool.join()