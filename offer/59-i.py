# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/15 17:40
'''
solution1: 暴力解法
solution2: 借鉴最小栈那道题的思路，使用一个队列保存滑动窗口内最大的值，并将该值存放在队头。
'''
import collections

class Solution:
    def maxSlidingWindow_1(self, nums, k: int):
        if len(nums) == 0:
            return []
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindow_2(self, nums, k):
        deque = collections.deque()
        res, n = [], len(nums)
        # i,j分别为滑动窗口的左右边界
        for i, j in zip(range(1 - k, n - k + 1), range(n)):
            # 如果队列第一个数是被删除的数，那么将这个数弹出，也就是队列中只能存储滑动窗口内的数字
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 如果队列的最后一个比当前要进入队列的数字要小，那么将这个数弹出，因为要保证队列中的是滑动窗口中的最大的数
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 用来判断是否进入滑动窗口
            if i >= 0:
                res.append(deque[0])
        return res


solution = Solution()
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(solution.maxSlidingWindow_2(nums, k))
