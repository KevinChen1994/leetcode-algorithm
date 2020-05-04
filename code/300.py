# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/3 22:50
'''
solution1: 动态规划。初始化状态转移矩阵全部为1，遍历到某个数字时，再遍历一遍这个数字之前的全部数字，如果之前的数字比当前数字小，那么就可以在那个数字的基础上加1来更新状态矩阵。
solution2: 对solution1的优化，用到了贪心算法和二分查找。维护一个tail数组，用来存储最长的上升序列。在遍历过程中，如果遇到的数比tail数组最后一个还大，那么直接放到tail后，
如果没有tail最后一个大，考虑是否比tail内的某个数大，可以进行替换，因为要保证tail是最长的上升序列，所以tail内的数要保证尽量小。在这个过程中用到了二分查找，即找到tail中
最大的小于当前数的那个数。二分查找时间复杂度为O(logN)，还需要将nums全部遍历一遍，整体的时间复杂度为O(NlogN)

'''
class Solution:
    def lengthOfLIS_1(self, nums):
        if len(nums) == 0: return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

    def lengthOfLIS_2(self, nums):
        if len(nums) == 0: return 0
        tail = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            # 使用二分查找法，在有序数组 tail 中
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = left + (right - left) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)



if __name__ == '__main__':
    solution = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    # nums = [10, 9, 2, 5, 3, 4]
    print(solution.lengthOfLIS_2(nums))
