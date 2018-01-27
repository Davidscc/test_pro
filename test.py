#!usr/bin/env python
# -*- coding:utf-8 -*-

import multiprocessing
import array

temp = array.array('i', [11,22,33,44])

def Foo(i):
    temp[i] = 100+i
    for item in temp:
        print(i, '----->', item)
if __name__ == '__main__':
    for i in range(2):
        p = multiprocessing.Process(target=Foo, args=(i,))
        p.start()

