# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/17 13:51
'''
solution: 使用异或运算，两个数相同为0，不同为1；因为异或操作满足交换律，例如:1^2^2=2^2^1=0^1=1（0异或任意数是等于任意数本身）
'''
class Solution:
    def singleNumber(self, nums):
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2]
    print(solution.singleNumber(nums))
