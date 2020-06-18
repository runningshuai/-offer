"""
题目描述
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
思路：层次遍历
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 层粒度遍历
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        queue = [pRoot] # 这一层进队列的节点，全部出队列
        high = 0
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            high += 1
        return high

# 下面的这种解法不行，同一层的左右节点，没有一次遍历，分成了两次。
# 这样遍历的结果是最终的层次遍历，但遍历的力度是左/右节点粒度，不是层粒度，这种做法不适合本题
class Solution1:
    def TreeDepth(self, pRoot):
        # write code here
        queue = [pRoot]
        high = 1
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            high += 1
        return high
