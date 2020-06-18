"""
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
来自牛客
看到这个问题, 我们最开始可能会想, 添加一个成员变量用于保存最小元素, 每次压栈时如果压栈元素比当前最小元素更小, 就更新最小元素.
    但是这样会有一个问题, 如果最小元素被弹出了呢, 如何获得下一个最小元素呢? 分析到这里可以发现, 仅仅添加一个成员变量存放最小元素是不够的, 我们需要在最小元素弹出后还能得到次小元素, 次小的弹出后, 还要能得到次次小的.
    因此, 用另一个栈来保存这些元素是再合适不过的了. 我们叫它最小元素栈.
    每次压栈操作时, 如果压栈元素比当前最小元素更小, 就把这个元素压入最小元素栈, 原本的最小元素就成了次小元素. 同理, 弹栈时, 如果弹出的元素和最小元素栈的栈顶元素相等, 就把最小元素的栈顶弹出.
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.A = []
        self.B = []
    def push(self, node):
        # write code here
        self.A.append(node)
        if not self.B:
            self.B.append(node)
        elif self.B[-1] > node:
            self.B.append(node)
    def pop(self):
        # write code here
        if self.A[-1] == self.B[-1]:
            self.B.pop()
        return self.A.pop()
    def top(self):
        # write code here
        return self.A[-1]
    def min(self):
        # write code here
        return self.B[-1]