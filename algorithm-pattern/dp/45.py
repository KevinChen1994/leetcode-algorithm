# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/23 14:54
'''
solution: 思想就是挨个挑，同时记录下能跳到的最远距离和当前位置能达到的边界。如果遍历到的位置到达了边界，那就去更新这个边界和更新步数。
'''
class Solution:
    def jump(self, nums):
        max_position = 0
        end = 0
        steps = 0
        for i in range(len(nums) - 1):
            # 在遍历过程中每次都记录可以跳到的最远位置
            max_position = max(max_position, nums[i] + i)
            # 如果当前位置到了边界位置，使用可以跳到的最远位置来进行更新边界，同时更新步数
            if i == end:
                end = max_position
                steps += 1
        return steps


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 1, 1, 4]
    print(solution.jump(nums))
