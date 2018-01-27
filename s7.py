#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process,Manager

def Foo(i, dic):
    dic[i] = 100 + i
    print(dic.values())

if __name__ == '__main__':
    manage = Manager()
    dic = manage.dict()
    for i in range(2):
        p = Process(target=Foo, args=(i, dic,))
        p.start()
        p.join()