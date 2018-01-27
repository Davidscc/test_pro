#!usr/bin/env python
# -*- coding:utf-8 -*-
import multiprocessing

li = []

def foo(i):
    li.append(i)
    print(li)
if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=foo, args=(i,))
        p.start()