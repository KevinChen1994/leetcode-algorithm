# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/17 17:47
# software: PyCharm
'''
solution1: 暴力法，两次for循环，每次找出区间内最小的值，乘上区间长度。
solution2: 分治算法。通过观察可以得出：确定了最矮柱子以后，矩形的宽尽可能往两边延伸。在最矮柱子左边的最大面积矩形（子问题）。
在最矮柱子右边的最大面积矩形（子问题）。每次记录最大的值进行比较。
solution3: 使用栈。
'''


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
            # 如果栈顶元素所代表的值大于当前的值，那么进行计算面积。
            while stack and heights[stack[-1]] > heights[i]:
                # 取出栈顶元素
                tmp = stack.pop()
                # 面积计算方法： 栈顶元素的所代表的值*（当前的索引-栈顶元素弹出之后的栈顶元素-1）
                # 原因：因为栈内的元素都是遇到比自己大的值才入栈，否则就进行计算面积了，所以栈内元素所代表的值都是从小到大排列的
                # 那么栈顶元素即为最大的那个值，他的面积也就是当前索引减去栈顶后边那个索引在减去1，建议结合实例走一遍流程就理解了。
                max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
            stack.append(i)
        return max_area

if __name__ == '__main__':
    solution = Solution()
    height = [2, 1, 5, 6, 2, 3]
    # height = [6, 4, 5, 2, 4, 3, 9]
    # height = [2, 2, 1, 2, 2]
    print(solution.largestRectangleArea_3(height))
