"""
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4,。
"""
# 还有更猛的 BFPRT
# -*- coding:utf-8 -*-
# 这个方法不好
class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 第一印象，堆排序
        if k > len(tinput):
            return []
        return self.heap_sort(tinput, k)[::-1]

    def heap_sort(self, arr, k):
        length = len(arr)
        # 构建堆
        for i in range(length//2 - 1, -1, -1):
            self.adjust(i, length - 1, arr)
        # 调整堆
        for j in range(length-1, length - k - 1, -1):
            arr[0], arr[j] = arr[j], arr[0]
            self.adjust(0, j - 1, arr)
        return arr[length - k:]

    def adjust(self, low, high, arr):
        # 小顶堆，low要调整的节点，high最后一个索引
        i = low
        j = 2 * i + 1
        while j <= high:
            if j < high and arr[j] > arr[j+1]:
                j += 1
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i = j
                j = 2*i + 1
            else:
                break
# 建数量为k的大顶堆，维护k个最小的元素。维护措施，堆顶最大元素和数组的元素比较，比堆顶小就加入，然后调整
class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput):
            return []
        return self.heap_sort(tinput, k)

    def heap_sort(self, arr, k):
        length = len(arr)
        # 构建堆，前k个元素
        for i in range(k//2 - 1, -1, -1):
            self.adjust(i, k - 1, arr)
        print(arr)
        # 维护堆
        for j in range(k, length):
            if arr[0] > arr[j]:
                arr[0], arr[j] = arr[j], arr[0]
                self.adjust(0, k-1, arr)
                # 调整堆
        for j in range(k - 1, -1, -1):
            arr[0], arr[j] = arr[j], arr[0]
            self.adjust(0, j - 1, arr)
        return arr[:k]

    def adjust(self, low, high, arr):
        # 大顶堆，low要调整的节点，high最后一个索引
        i = low
        j = 2 * i + 1
        while j <= high:
            if j < high and arr[j] < arr[j+1]:
                j += 1
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i = j
                j = 2*i + 1
            else:
                break
s = Solution2()
print(s.heap_sort([4,5,1,6,2,7,3,8],4))