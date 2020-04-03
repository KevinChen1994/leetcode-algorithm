# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/4/3 16:09
# software: PyCharm
'''
solution1: 在遍历过程中，如果当前的数字还出现在nums不包含当前数字的列表中，那他就是出现两次的数字。
solution2: 数学运算。nums去重复的两倍减去nums的和，剩下的就是出现一次的数字
solution3: 位操作。当前数字异或0结果还是当前数字，当前数字异或相同的数字等于0，同时满足交换律。
'''
class Solution:
    def singleNumber_1(self, nums):
        for i, num in enumerate(nums):
            if num not in nums[0:i] + nums[i + 1:]:
                return num

    def singleNumber_2(self, nums):
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber_3(self, nums):
        a = 0
        # ^表示异或运算
        for i in nums:
            a ^= i
        return a


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1, 2, 4]
    print(solution.singleNumber_3(nums))
