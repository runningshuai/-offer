"""
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
可以模拟魔方逆时针旋转的方法，一直做取出第一行的操作
例如
1 2 3
4 5 6
7 8 9
输出并删除第一行后，再进行一次逆时针旋转，就变成：
6 9
5 8
4 7
继续重复上述操作即可。
"""

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix:
            return matrix
        if len(matrix)==1:
            return matrix[0]
        result = []
        while matrix:
            result.extend(matrix.pop(0))
            matrix = self.turn(matrix)
        return result
    # 转置
    def turn(self, A):
        if not A:
            return A
        row = len(A)
        col = len(A[0])
        result = []
        for j in range(col-1, -1, -1):
            temp = []
            for i in range(row):
                temp.append(A[i][j])
            result.append(temp)
        return result