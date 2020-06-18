"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
思路
从下到上，找第一个比target小的数，然后向右找，若找到则返回True，找不到返回False
"""


# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array) <= 1:
            return False
        row_length = len(array)
        col_length = len(array[0])
        # 遍历
        for row in range(row_length-1, -1, -1):
            if array[row][0] <= target:
                for col in range(col_length):
                    if array[row][col] == target:
                        return True
        return False


if __name__ == '__main__':
    arr = [[1, 2, 8, 9],
           [2, 4, 9, 12],
           [4, 7, 10, 13],
           [6, 8, 11, 15]]
