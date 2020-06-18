"""
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：
快慢指针p1 ,p2（2倍速）
          *  *
----a---*      * b 相遇点
          *  *
假设根节点到环的入口节点为a，以入口节点为参照物，在据入口节为b的位置相遇
在第一次相遇点p1走的距离：a+b
假设环长t,则p2走了： a + b + k*t(k圈) = 2（a+b）
得出a+b = k*t，对于快指针p2，现在距离环入口b,它只要再走a，就一定到达环入口
再让慢指针从根节点开始走a，相遇了就是环入口
"""
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        p1 = pHead.next
        p2 = pHead.next.next
        while p1.val != p2.val:
            if p1 and p2.next:
                p1 = p1.next
                p2 = p2.next.next
            else:
                return None
        # 一起走a步，同步走
        while pHead.val != p2.val:
            pHead = pHead.next
            p2 = p2.next
        return pHead