# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/13 21:22
'''
solution1: 使用字典存储每一个出现的数字及出现的次数，然后进行判断。
solution2: 将列表进行排序，出现次数高于list数量一半的数肯定会在排好序的list中间位置存在。
'''
class Solution:
    def majorityElement_1(self, nums) -> int:
        dict_ = {}
        for num in nums:
            if num in dict_:
                dict_[num] += 1
            else:
                dict_[num] = 1
        for d in dict_:
            if dict_[d] > len(nums) / 2:
                return d
    def majorityElement_2(self, nums):
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 3]
    print(solution.majorityElement_2(nums))
