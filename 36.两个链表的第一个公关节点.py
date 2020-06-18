"""
题目描述
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，
所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的
思路：
找出2个链表的长度，然后让长的先走两个链表的长度差，然后再一起走
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        n1 = self.link_length(pHead1)
        n2 = self.link_length(pHead2)
        # 长的先走长度之差
        if n1 > n2:
            num = n1 - n2
            while num:
                pHead1 = pHead1.next
                num -= 1
        else:
            num = n2 - n1
            while num:
                pHead2 = pHead2.next
                num -= 1
        # 一起走
        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

    def link_length(self, head):
        if not head:
            return 0
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length