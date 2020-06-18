"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：
就数组的最小值
1、若扫描一遍，可求出最小值，但不是好的方法
2、利用二分法，只不过数组旋转之后，变成了两部分有序的数组，需要变形一下
"""
# -*- coding:utf-8 -*-
class Solution1:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        m = rotateArray[0]
        for i in range(1, len(rotateArray)):
            if rotateArray[i] < m:
                m = rotateArray[i]
        return m

# 二分查找变形,特殊的但拉出来处理，和左边进行比较，查找mid
class Solution2:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        mid = left + (right - left)//2
        if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
            m = rotateArray[0]
            for i in range(1, len(rotateArray)):
                if rotateArray[i] < m:
                    m = rotateArray[i]
                    return m
        while rotateArray[left] >= rotateArray[right]:
            # 这里不用(left + right)//2是为了防止left + right过大导致溢出，但python对整型不会溢出
            if right -left == 1:
                mid = right
                break
            mid = left + (right - left)//2
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                m = rotateArray[0]
                for i in range(1, len(rotateArray)):
                    if rotateArray[i] < m:
                        m = rotateArray[i]
                return m
            if rotateArray[left] <= rotateArray[mid]:
                # mid在左数组
                left = mid
            elif rotateArray[left] > rotateArray[mid]:
                # mid在右数组
                right = mid
        # left,right的最后结果，左边数组的最后一个，right是右边数组的第一个
        return rotateArray[mid]


# 和最右边的数字比较
class Solution3:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while left < right:
            # 这里不用(left + right)//2是为了防止left + right过大导致溢出，但python对整型不会溢出
            mid = left + (right - left)//2
            if rotateArray[right] < rotateArray[mid]:
                # mid在左数组
                left = mid + 1
            elif rotateArray[right] > rotateArray[mid]:
                # mid在右数组
                right = mid
            else:
                # 0 1 1 1 1旋转后 1 0 1 1 1，要挨个找
                right = right - 1
        # left,right的最后结果，左边数组的最后一个，right是右边数组的第一个
        return rotateArray[right]