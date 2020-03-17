# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/17 17:47
# software: PyCharm

class Solution:
    # 暴力法
    def largestRectangleArea_1(self, heights):
        max_area = 0
        for i in range(0, len(heights)):
            min_len = float('inf')
            for j in range(i, len(heights)):
                min_len = min(min_len, heights[j])
                max_area = max(max_area, min_len * (j - i + 1))
        return max_area

    # 分治算法
    def largestRectangleArea_2(self, heights):
        max_area = self.calculate_area(heights, 0, len(heights))
        return max_area

    def calculate_area(self, heights, start, end):
        if start > end:
            return 0
        min_index = start
        for i in range(start, end):
            if heights[i] < heights[min_index]:
                min_index = i
        return max(heights[min_index] * (end - start + 1),
                   max(self.calculate_area(heights, start, min_index - 1),
                       self.calculate_area(heights, min_index + 1, end)))

    # 栈
    def largestRectangleArea_3(self, heights):
        stack = []
        max_area = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                max_area = max(max_area, heights[tmp] * (i-stack[-1]-1))
            stack.append(i)
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [2, 1, 5, 6, 2, 3]
    # height = [6, 4, 5, 2, 4, 3, 9]
    print(solution.largestRectangleArea_3(height))
