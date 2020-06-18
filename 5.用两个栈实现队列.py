"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
思路
栈A用来入队列
栈B用来出队列，即反转栈A，也就是栈A出栈到栈B，栈B再出栈，就实现了出队列
"""


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, node):
        # write code here
        self.A.append(node)

    def pop(self):
        # return xx
        # 出队列的内容全来自A
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop()
