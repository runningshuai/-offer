"""
题目描述
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
思路：
不能用乘除法：排除通向公式n*(n+1)/2
不能用for, while排除累加
不能用if 递归终止条件无法用，这里用与的短路效应来结束递归
这里全部变量用self.才可以，不知道为啥？
"""
class Solution:
    global res
    res = 0
    def Sum_Solution(self, n):
        # write code here
        global res
        (n > 1) and self.Sum_Solution(n - 1)
        res += n
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.Sum_Solution(2))