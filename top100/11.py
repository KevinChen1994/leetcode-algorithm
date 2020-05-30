# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/15 11:03
# software: PyCharm

class Solution:
    # 双指针，前后各一个指针，高度较小的指针移动，直到两个指针重合，记录过程中所有面积，求出最大面积
    def maxArea(self, height):
        if len(height) == 0:
            return 0
        max = 0
        start = 0
        end = len(height) - 1
        while start != end:
            area = (end - start) * min(height[start], height[end])
            if area > max:
                max = area
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
