# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/5 21:30
'''
solution1: 使用最多的方法。因为nums内的数字大小为[0...n-1]，如果没有重复数字的话，那么每个数字应该在与他相等的索引上，
现在有重复数组，所以如果nums排序后，数字没有在他对应的索引的数字一定是重复数字。
solution2: 最容易想到的方法，但是注意要使用set(),不要使用list(),list会比set慢很多，会超时。
'''
class Solution:
    def findRepeatNumber_1(self, nums) -> int:
        for i in range(len(nums)):
            while nums[i] != i:
                # 因为当前num肯定跟索引不同，所以当当前num跟以num为索引的数字相同时，证明有重复数字
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                # 按照数字的大小放到对应的索引上去。
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

    def findRepeatNumber_2(self, nums):
        set_ = set()
        for num in nums:
            if num not in set_:
                set_.add(num)
            else:
                return num


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(solution.findRepeatNumber_2(nums))