"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
 思路：
 扫描指针temp
 跳转指针pre, pre的头节点head
 pre和head要在temp的前一位
 temp要能走到最后一个节点
"""
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead:
            return
        head = ListNode(0)
        head.next = pHead
        pre = head
        temp = pHead
        while temp:
            if temp.next and temp.val == temp.next.val:
                while temp.next and temp.val == temp.next.val:
                    temp = temp.next
                pre.next = temp.next
                temp = temp.next
            else:
                temp = temp.next
                pre = pre.next
        return head.next


