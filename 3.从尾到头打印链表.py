"""
输入一个链表，按链表从尾到头的顺序返回一个ArrayList
思路
法一：利用栈 和 队列，进栈和出栈实现反序，队列接受出栈结果返回
法二：利用递归，递归来实现反序，队列存储结果
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        stack = []
        res = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        while stack:
            res.append(stack.pop())
        return res

# 递归
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        res = []
        if listNode:
            res = self.printListFromTailToHead(listNode.next) # 只有返回结果才继续往下执行
            res.append(listNode.val)
        return res
