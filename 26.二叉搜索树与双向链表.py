"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        stack = []
        head = None
        pre = None # 前置节点
        cur = pRootOfTree
        while stack or cur:
            if cur:
                # 遍历左子树
                stack.append(cur)
                cur = cur.left
            else:
                # root为空
                pop = stack.pop()
                if not head:
                    head = pop
                    pre = pop
                else:
                    pre.right = pop
                    pop.left = pre
                    pre = pop
                cur = pop.right
        return head
