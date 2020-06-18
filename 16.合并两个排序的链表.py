"""
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        new = None
        p1 = pHead1
        p2 = pHead2
        if pHead1.val > pHead2.val:
            new = pHead2
            p2 = pHead2.next
        else:
            new = pHead1
            p1 = pHead1.next
        head = new # 保存头节点，new一直next到最后
        while p1 and p2:
            if p1.val < p2.val:
                new.next = p1
                p1 = p1.next
            else:
                new.next = p2
                p2 = p2.next
            new = new.next  # 要移动，new成为最后一个节点

        if not p1:
            new.next = p2
        if not p2:
            new.next = p1
        return head