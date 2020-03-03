# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/2 21:38
# software: PyCharm

'''
solution1: 按行计算。遍历每一行的元素，当遇到比行数大的数开始计算（flag = True），之后遇到比行数小的数tmp加1，一直到遇到比行数大的数，
将tmp的值累加到ans中，并将tmp归零。时间复杂度为O(m*n)
solution2: 按列计算。遍历每一列元素，找到当前列左边最大的元素以及右边最大的元素，根据木桶效应，水的高度最多到两个墙最矮的高度，记这个高度为min_other。
分为三种情况：1 当前元素大于min_other，那么当前元素上不会有水；2 当前元素小于min_other，那么当前元素上的水的高度为min_other减去当前元素的大小；
3 当前元素等于min_other，那么当前元素上也不会有水。时间复杂度为O(n²)
solution3: 动态规划。对solution2的优化，分别遍历一遍所有元素，找到当前要素左边最大与右边最大，然后再遍历一遍要素找到水的体积。时间复杂度O(n)
'''


class Solution:
    # 按行计算
    def trap_1(self, height):
        max_height = max(height)
        ans = 0
        for i in range(1, max_height + 1):
            flag = False
            tmp = 0
            for j in range(len(height)):
                if flag and height[j] < i:
                    tmp += 1
                if height[j] >= i:
                    flag = True
                    ans += tmp
                    tmp = 0
        return ans

    # 按列计算
    def trap_2(self, height):
        ans = 0
        for i in range(1, len(height) - 1):
            current_height = height[i]
            left_max = 0
            right_max = 0
            # 找到当前列左边最高的墙
            for i in range(0, i):
                if height[i] > left_max:
                    left_max = height[i]
            # 找到当前列右边最高的墙
            for i in range(i + 1, len(height)):
                if height[i] > right_max:
                    right_max = height[i]
            min_other = min(left_max, right_max)
            if current_height < min_other:
                ans += (min_other - current_height)
        return ans

    # 动态规划
    def trap_3(self, height):
        ans = 0
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i - 1], height[i - 1])
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, len(height)):
            min_other = min(max_left[i], max_right[i])
            if height[i] < min_other:
                ans += min_other - height[i]
        return ans

    # 双指针
    def trap_4(self, height):
        ans = 0
        max_left = 0
        max_right = [0] * len(height)
        for i in range(len(height) - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i + 1])
        for i in range(1, len(height)):
            max_left = max(max_left, height[i - 1])
            min_other = min(max_left, max_right[i])
            if height[i] < min_other:
                ans += min_other - height[i]
        return ans


if __name__ == '__main__':
    solution = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    # height = [2, 0, 2]
    print(solution.trap_4(height))
