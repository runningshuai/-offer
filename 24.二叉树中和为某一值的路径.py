"""
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
思路
这题难点在于记录路径，需要两个全局变量，记录某一条的路径为path，全部路径为result
注意：递归，它其实是一条路径一条路径找的，找路径的方式按先序遍历找
找第一条路径，都是递，然后是归，找第二条路径继续递
就这样一直 递、归 递、归 就遍历完了所有路径，并返回起点
递归有遍历的作用.
有一处坑，在result.append(list(path))
"""
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.path = []
        self.result = []

    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.path.append(root.val)
        # 只在递归到叶子节点的时候才有完整的一条路径path,在这里加入总的列表result中
        if root.val == expectNumber and not root.left and not root.right:
            # 记录路径时若直接执行 res.append(path) ，则是将 path 列表对象 加入了 res ；
            # 后续 path 对象改变时， res 中的 path 对象 也会随之改变
            #（因此肯定是不对的，本来存的是正确的路径 path ，后面又 append 又 pop 的，就破坏了这个正确路径）。
            #list(path) 相当于新建并复制了一个 path 列表，因此不会受到 path 变化的影响。
            self.result.append(list(self.path))
        # 考虑递归到半路，目标值为负了，提前返回
        if expectNumber < 0:
            return False
        if root.left:
            self.FindPath(root.left, expectNumber - root.val)
        if root.right:
            self.FindPath(root.right, expectNumber - root.val)
        # 最重要的，走到这里，path已经完整的记录了一条路径了，且存到result了，需要把最后一次加入的节点去除
        # 因为该函数返回之后，会执行相应的右节点/子树，需要把path还原，可以说path也跟着回到上一个状态
        self.path.pop()
        # 能走到这里都是找到的一条路径，返回True，其实这里只要return就行了，不需要知道返回什么
        return self.result



