"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""
# 暴力搜索，时间复杂度过大，行不通
class Solution1:
    def InversePairs(self, data):
        # write code here
        length = len(data)
        total = 0
        for i in range(length):
            for j in range(i+1, length):
                if data[i] > data[j]:
                    total += 1
        return total

class Solution2:
    def __init__(self):
        self.count = 0
    def InversePairs(self, data):
        # write code here
        # 利用归并排序的分治思想

        self.expand(data)
        return self.count

    def merge(self, arr1, arr2):
        # l1, l2 = len(arr1), len(arr2)
        # m = l1 - 1
        # while m >= 0:
        #     n = l2 - 1
        #     while n >= 0:
        #         if arr1[m] > arr2[n]:
        #             self.count += n + 1
        #             break
        #         else:
        #             n -=1
        #     m -= 1
        # 以上过程可以合进同一个循环，加两个循环还是会超时

        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
                self.count += len(arr1) - i
        if i == len(arr1):
            res.extend(arr2[j:])
        if j == len(arr2):
            res.extend(arr1[i:])
        return res

    def expand(self, data):
        length = len(data)
        if length == 1:
            return data
        index = length//2
        left = self.expand(data[:index])
        right = self.expand(data[index:])
        return self.merge(left, right)

s2 = Solution2()
result = s2.InversePairs([1,2,3,4,5,6,7,0])
print(result)