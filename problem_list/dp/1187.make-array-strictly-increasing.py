# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/4 22:02
from typing import List
'''
参考：https://www.acwing.com/file_system/file/content/whole/index/content/5467/
solution: 定义dp[i][j]为arr1前i个（包括i），使用最少操作数j构成的递增数组，值为第i位的最小值。
首先需要将arr2去重排序，去重的原因是后边需要二分查找找到第一个比x大的索引，如果不去重，找到的可能等于x。
然后定义dp矩阵，宽为arr1的长度加1，因为可能有arr1的长度的操作次数，当然也可以用arr2的长度作为宽，最大的操作数为arr2的长度；长为arr1的长度。
dp[0][0]的意思为arr1长度为1，操作数为0，那最小值就是arr1的第一个数字；
dp[0][1]的意思为arr1长度为1，操作数为1，也就是替换了一次，所以最小值为排序后的arr2的第一个。
转移矩阵比较难想，首先判断arr1当前第i个字符是否大于dp[i-1][j]，dp[i-1][j]的值为前i-1个在第j个操作数下最小值，
如果大于说明是递增的序列，这里肯定是不操作，但是最小值需要选择一下，那么选择使用arr1[i]或者dp[i][j]中最小的，因为dp[i][j]可能已经计算过了，可能比arr1[i]要小。
另外还需要判断dp[i-1][j-1]是否已经替换过了，如果替换过，那dp[i][j]需要替换为比dp[i-1][j-1]大的第一个数，这里需要用二分查找来做。
总之状态转移矩阵需要做的事情，就是找到dp[i][j]下最小的数，其来源可能是不变，或者比上一个大的第一个数。
最终判断就是在dp[i][j]的第i行，也就是长度为arr1的长度下，最小的操作数。

PS:Python有一个库bisect，已经实现了通过二分查找来找到target的左边界右边界。https://docs.python.org/zh-cn/3.6/library/bisect.html
'''

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        l1 = len(arr1)
        l2 = len(arr2)
        arr2 = list(set(arr2))
        arr2.sort()
        dp = [[float('inf') for _ in range(l1 + 1)] for _ in range(l1)]
        dp[0][0] = arr1[0]
        dp[0][1] = arr2[0]
        for i in range(1, l1):
            for j in range(i + 2):
                if arr1[i] > dp[i - 1][j]:
                    dp[i][j] = min(dp[i][j], arr1[i])
                if j > 0:
                    if dp[i - 1][j - 1] < float('inf'):
                        up = self.binary_search(arr2, dp[i - 1][j - 1])
                        if up != -1:
                            dp[i][j] = min(dp[i][j], arr2[up])
        for i in range(l1 + 1):
            if dp[-1][i] != float('inf'):
                return i

        return -1

    # 找到第一个大于target的索引
    def binary_search(self, arr, target):
        if target >= arr[-1]:
            return -1
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                return mid + 1
        return right


if __name__ == '__main__':
    solution = Solution()
    # arr1 = [1, 5, 3, 6, 7]
    # arr2 = [1, 3, 2, 4]
    # arr1 = [1, 5, 3, 6, 7]
    # arr2 = [4, 3, 1]
    arr1 = [1, 5, 3, 6, 7]
    arr2 = [1, 6, 3, 3]

    print(solution.makeArrayIncreasing(arr1, arr2))
