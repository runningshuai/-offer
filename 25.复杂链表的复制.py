"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
# -*- coding:utf-8 -*-


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution1:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # 广度优先遍历
        # 记录已经遍历的，下次遇到直接连接
        head = RandomListNode(pHead.label)
        visited = {pHead: head}
        # 队列，负责查找下一个节点，也就是遍历
        queue = [pHead]
        while queue:
            pop = queue.pop(0)
            # 复制
            if pop.next and pop.next not in visited:
                queue.append(pop.next)
                visited[pop.next] = RandomListNode(pop.next.label)
            if pop.random and pop.random not in visited:
                queue.append(pop.random)
                visited[pop.random] = RandomListNode(pop.random.label)
            # 连接
            visited[pop].next = visited[pop.next]
            visited[pop].random = visited[pop.random]
        return head

# 1、在原链表上分别复制节点，并分别紧跟其后 2、连接random节点 3、拆分复制链表
class Solution2:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
            # 1、复制
        cur = pHead
        while cur:
            new = RandomListNode(cur.label)
            # 新的连接到后面
            new.next = cur.next
            # cur连接新的节点
            cur.next = new
            # 节点后移
            cur = cur.next.next

        # 2、连接random
        cur = pHead  # pHead节点没有跟着往后移动
        while cur:
            # random也要指向新的复制的节点，cur.random是老的，新的在老的后面cur.random.next
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        # 3、拆分
        old = pHead
        new_list = pHead.next
        result = pHead.next
        while old:
            old.next = old.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old = old.next
            new_list = new_list.next
        return result


# 递归解法，让next递归，random跟随其后进行连接。只递归一个指针
class Solution3:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        new = RandomListNode(pHead.label)
        new.next = self.Clone(pHead.next)
        new.random = pHead.random
        return new
