# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/5 17:34
# software: PyCharm
'''
solution1 贪心算法。tmp用来存放连续序列的和，如果tmp小于0，那么这个序列加上后边的一个数，必定会小于这个数，所以这个序列带来的影响就是负面的影响，
对于这种情况，直接舍弃掉，将tmp置为当前值。如果序列之和大于0，那么这个序列加上后边的数带来的是增益效果，那么就做一个累加的操作。
那么如果都是负数呢？那tmp会永远小于0，在做完判断后会取一个最大值，那么这个最大值就是当前全部序列中的最大序列之和，因负数相加只会变小。
solution2 分治算法。将整个序列分成几个小组，每个小组再切成更小的组，一直到不能切分为止，每个小组会计算出最优解，汇报给上一级的小组，一级一级汇报，
直到得到最终结果。参考https://leetcode-cn.com/problems/maximum-subarray/solution/zheng-li-yi-xia-kan-de-dong-de-da-an-by-lizhiqiang/
'''


class Solution:
    # 贪心算法
    def maxSubArray_1(self, nums):
        max_ = nums[0]
        tmp = 0
        for i in range(len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            max_ = max(max_, tmp)
        return max_

    # 分治算法
    def maxSubArray_2(self, nums):
        if len(nums) == 1:
            return nums[0]
        else:
            # 找到左半部分最大的序列，通过递归去找。
            left_sum = self.maxSubArray_2(nums[0:len(nums) // 2])
            # 找到有半部分最大的序列
            right_sum = self.maxSubArray_2(nums[len(nums) // 2:len(nums)])
        # 包含左半部分右边元素的最大值
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2-1,-1,-1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        tmp = 0
        # 包含右半部分左边元素的最大值
        max_r = nums[len(nums) // 2]
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(max_r, tmp)
        return max(left_sum, right_sum, max_l + max_r)




if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums = [-2, 1 ]
    # nums = [-2, -1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray_2(nums))
