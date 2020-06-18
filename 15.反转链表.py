"""
题目描述
输入一个链表，反转链表后，输出新链表的表头
需要三个指针
pre, temp, next
带反转的节点为temp,已经反转好的为pre, 未来要反转的节点next
步骤
1、当前节点temp要和未来断开，要保存未来要反转的节点，next = temp.next
2、和未来断开，断开了要反向指向，也就是已经反转好的pre，temp.next = pre，这里断开未来节点的同时又连接以前（断开又连接）
3、temp已经反转好了，把pre指向反转好的temp节点（也就是反转好的额最后一个节点），pre = temp
4、temp要指向下一个要反转的节点（之前保存的next）,temp = next
"""


# 不能借助辅助空间，在原链表上反转
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        temp = pHead
        next = None
        while temp:
            next = temp.next
            temp.next = pre
            pre = temp
            temp = next
        return pre