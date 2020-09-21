# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/21 21:26
'''
solution1: 最笨的方法，使用字典统计每个数字的个数
solution2: 使用摩尔投票法，当前数字等于x时，加1，否则减1。这样如果x不是出现次数最多的数字，最终就会被抵消掉。
solution3:
'''


class Solution:
    def majorityElement_1(self, nums) -> int:
        dic = {}
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
                if dic[num] > len(nums) // 2:
                    return num

    def majorityElement_2(self, nums):
        vote = 0
        for num in nums:
            if vote == 0:
                x = num
            vote += 1 if num == x else -1
        return x

    def majorityElement_3(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(solution.majorityElement_3(nums))
