# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/27 22:36
'''
solution1: 暴力法，计算每一个滑动窗口内的最大值。
solution2: 双向队列。首先构建一个队列，队列中存放的是不超过滑动窗口大小的nums的索引，在遍历K个元素后的数组时，需要对队列进行清理：1.队列的大小不能超过滑动窗口；
2.队列内的索引对应的元素不能大于当前元素，当前元素即为即将要入队的元素。清理完队列后，将当前元素入队，此时队列的第一个元素就是当前滑动窗口的最大的元素。
solution3: 与solution2思路类似
'''
from _collections import deque


class Solution:
    def maxSlidingWindow_1(self, nums, k):
        length = len(nums)
        ans = []
        for i in range(length - k + 1):
            ans.append(max(nums[i:k + i]))
        return ans

    def maxSlidingWindow_2(self, nums, k):
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        # 始终保持队列中的元素不超过滑动窗口的大小，并且队列的开头是最大的元素的索引，
        # 如果队列中的所有元素都没有当前元素大的话，那么这个队列就变成了空队列。
        def clean_deque(i):
            # 移除队列中不在滑动窗口内的元素
            if deq and deq[0] == i - k:
                deq.popleft()

            # 移除队列中所有比当前元素小的元素
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # 初始化队列，并选出其中最大的元素，放入到output中
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output

    def maxSlidingWindow_3(self, nums, k):
        temp = [nums[0]]
        res = [max(nums[0:k])]
        for i in range(1, k):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
        n = len(nums)
        for i in range(k, n):
            if nums[i - k] >= temp[0]:
                del temp[0]
            if not temp:
                temp.append(max(nums[i - k + 1:i + 1]))
            elif nums[i] >= temp[-1]:
                temp.append(nums[i])
            res.append(temp[-1])
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solution.maxSlidingWindow_2(nums, k))
