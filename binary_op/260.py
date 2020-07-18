# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/17 14:10
'''
solution: 想办法将nums分成两组，每组分别包含1个只出现一次的数字，两组分别异或就得到两个只出现一次的数字。
首先将全部数组进行异或，最终的结果就是两个只出现一次的数字的异或结果。如果某一位是1，就意味着另一个数组的这个位置是0。
'''
class Solution:
    def singleNumber(self, nums):
        bitmask = 0
        for num in nums:
            bitmask = bitmask ^ num
        # 保留bitmask最右边的1，这个1要么来自x，要么来自y
        diff = bitmask & (-bitmask)
        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    print(solution.singleNumber(nums))
