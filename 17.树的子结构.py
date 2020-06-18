"""
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 从根节点开始遍历（采用递归去遍历），查看根节点是否匹配，若匹配，则查看各自的左右子树是否匹配
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        # 两个根节点是否匹配上,有3种情况
        return (pRoot1.val == pRoot2.val and self.tree1_has_tree2(pRoot1, pRoot2)) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    # 这个函数，查看各自的左右子树是否匹配
    def tree1_has_tree2(self, root1, root2):
        # root2为空，不管root1是否为空都能匹配上
        if not root2:
            return True
        # 树1为空且树2不为空，则匹配不上
        if not root1 and root2:
            return False
        # root1和root2都不为空,若匹配不上则返回空
        if root1.val != root2.val:
            return False
        # root1和root2都不为空,若匹配上，则继续分别查看左右子树是否匹配上
        return self.tree1_has_tree2(root1.left, root2.left) and self.tree1_has_tree2(root1.right, root2.right)