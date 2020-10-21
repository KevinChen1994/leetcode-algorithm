# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/20 19:53

class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        joker = 0
        for i in range(4):
            if nums[i] == 0:
                joker += 1
            elif nums[i] == nums[i + 1]:
                return False
        # 最大牌减去最小牌小于5就是顺子
        return nums[4] - nums[joker] < 5



if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0, 2, 2, 5]

    print(solution.isStraight(nums))
