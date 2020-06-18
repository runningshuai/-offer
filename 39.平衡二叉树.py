"""
题目描述
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
在这里，我们只需要考虑其平衡性，不需要考虑其是不是排序二叉树
思路：
平衡二叉树由来
通过之前对二叉搜索树介绍可知，将集合构造为二叉搜索树结构，该结构下对树中节点的查询、删除和插入三种操作，
时间复杂度均为O(logN) - O(N)。
影响时间复杂度的因素即为二叉树的高，为了尽量避免树中每层上只有一个节点的情况，这里引入平衡二叉树。
定义：
平衡二叉树也叫自平衡二叉搜索树（Self-Balancing Binary Search Tree），所以其本质也是一颗二叉搜索树，
不过为了限制左右子树的高度差，避免出现倾斜树等偏向于线性结构演化的情况，
所以对二叉搜索树中每个节点的左右子树作了限制，左右子树的高度差称之为平衡因子，
树中每个节点的平衡因子绝对值不大于 ，此时二叉搜索树称之为平衡二叉树。
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 当子树不是二叉平衡树时，直接返回False,是整个判断结果，但当满足平衡二叉树时，需要返回树的高度，作为上一层函数判断的依据，
# 递归函数返回False,只是一个递归函数的结束返回，并不能作用于整个函数的结果。
# 所以，需要加个全局变量，若子树不满足，直接为False。

# 子树不满足时，并没有及时返回，还是遍历了整个树，有人在这种情况下通过抛出异常结束递归来达到不用遍历整棵树的目的
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        # 递归，高度≤1
        # 递归停止条件
        global isbalance
        isbalance = True
        self.get_depth(pRoot)
        return isbalance

    def get_depth(self, root):
        global isbalance
        if not root:
            return 0
        left = self.get_depth(root.left) + 1
        right = self.get_depth(root.right) + 1
        if abs(left - right) > 1:
            isbalance = False
        return max(left, right)
