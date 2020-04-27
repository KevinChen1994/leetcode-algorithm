# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/27 22:36

from _collections import deque
class Solution:
    def maxSlidingWindow_1(self, nums, k):
        length = len(nums)
        ans = []
        for i in range(length - k + 1):
            ans.append(max(nums[i:k + i]))
        return ans

    def maxSlidingWindow_2(self, nums, k):
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

    def maxSlidingWindow_3(self, nums ,k):
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(solution.maxSlidingWindow_3(nums, k))
