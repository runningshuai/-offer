"""
题目描述
统计一个数字在排序数组中出现的次数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        i, j = 0, len(data) - 1
        while i < j:
            mid = i + (j - i) // 2
            if data[mid] >= k:
                j = mid
            else:
                i = mid + 1
        count = 0
        for index in range(i, len(data)):
            if data[index] == k:
                count += 1
            else:
                break
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1, 2, 3, 3, 3, 4], 3))