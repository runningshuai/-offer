"""
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出
理解题意：
递增序列，找两个数和为S,不要求连续
"""

# 看了别人的思路，左右夹逼，复杂度O(N)
class Solution2:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i, j = 0, len(array) - 1
        result = []
        while i < j:
            temp = array[i] + array[j]
            if temp == tsum:
                result.append([array[i], array[j]])
                i += 1
            elif temp > tsum:
                j -= 1
            else:
                i += 1
        if not result:
            return []
        else:
            return result[0]


# 开始思路，先定一个数i，tsum - i进行二分查找，复杂度O(NlogN)
class Solution1:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        for i in range(length):
            m = array[i]
            n = tsum - m
            res = self.binary_search(array[i+1:], n)
            if res:
                return [m, n]
        return []

    def binary_search(self, arr, target):
        if not arr:
            return False
        i, j = 0, len(arr) - 1
        while i <= j:
            mid = (i + j)//2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return False

if __name__ == '__main__':
    s = Solution1()
    print(s.binary_search([2, 3, 4, 5, 6, 7, 8, 9], 9))
    print(s.FindNumbersWithSum([1, 2, 4, 6, 7, 8, 11, 16], 10))

    s2 = Solution2()
    print(s2.FindNumbersWithSum([1, 2, 4, 6, 7, 8, 11, 16], 10))
