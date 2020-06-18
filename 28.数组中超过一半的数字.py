"""
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
本题常见解法如下：
哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，最终超过数组长度一半的数字则为众数。此方法时间和空间复杂度均为 O(N)O(N) 。
数组排序法： 将数组 nums 排序，由于众数的数量超过数组长度一半，因此 数组中点的元素 一定为众数。此方法时间复杂度 O(N log_2 N)O(Nlog 2N)。
摩尔投票法： 核心理念为 “正负抵消” ；时间和空间复杂度分别为 O(N)O(N) 和 O(1)O(1) ；是本题的最佳解法。
摩尔投票法：
票数和： 由于众数出现的次数超过数组长度的一半；若记 众数 的票数为 +1+1 ，非众数 的票数为 -1−1 ，则一定有所有数字的 票数和 > 0>0 。
票数正负抵消： 设数组 nums 中的众数为 xx ，数组长度为 nn 。若 nums 的前 aa 个数字的 票数和 = 0=0 ，则 数组后 (n-a)(n−a) 个数字的 票数和一定仍 >0>0 （即后 (n-a)(n−a) 个数字的 众数仍为 xx ）。
"""
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        vote = 0
        m = numbers[0]
        for item in numbers:
            if item == m:
                vote += 1
            else:
                vote -= 1
            if vote == 0:
                m = item
                vote += 1
        # 验证
        count = 0
        for item in numbers:
            if item == m:
                count += 1
        if count > len(numbers)/2:
            return m
        else:
            return 0

s = Solution()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))