"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
理解题意：
数组筛选的候选是整个自然数，找出和为tsum的序列，要求连续
"""
# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        i, j = 1, 2
        # 不满足时，i会一直增加，直到超过j结束循环
        while i < j:
            temp = sum(range(i, j + 1))
            if temp == tsum:
                result.append(list(range(i, j + 1)))
                # 破坏相等条件
                i += 1
            elif temp < tsum:
                j += 1
            else:
                i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    res = s.FindContinuousSequence(100)
    print(res)