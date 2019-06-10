#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 22:35
# @Author  : liupeiyu
# @File    : 栈队列.py
# 本质上分为两个栈，一个只用来push，但是pop的时候需要分为两部分，如果stack2不空的时候就必须从stack2里pop，只要当stack 空的时候，必须一次性
# 把stack1都放进stack2里，才能保证先进先出，因为后面再push的话都得stack2这一波全空了才能把stack1再第二波再放进来。stack1和stack2在pop的过程中类似于两个part
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        self.stack1.append(x)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                x = self.stack1.pop()
                self.stack2.append(x)
            return self.stack2.pop()
solu = Solution()
solu.push(1)
solu.push(2)
print(solu.pop())