# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/15 11:12
'''
solution: 如果用暴力法很好解决，就是在遍历过程中，每个高度分别往左往右找到第一个比他小的数，在以当前元素为高，两个比他小的数为之间的长度为宽，进行相乘就是面积。这里可以借助栈降低时间复杂度，用空间换时间。
在遍历过程中，将大于当前元素的索引压入栈中，这样栈内的索引都是按照实际值的从小到大的顺序的，这样方便计算，接下来在遍历过程中，如果遇到元素比栈顶元素小，这时就要以栈顶元素所代表的元素为高进行计算面积了，
高确定了，那么宽就是当前元素索引减去弹出栈顶后下一个索引的差再减去1，具体原因为这两个索引分别是栈顶元素左边和右边第一个比他小的数，索引相减在减一是实际的宽度。
'''
class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            # 如果栈内索引所代表的元素大于当前元素，这时候就要以这个索引所代表的元素的高度计算面积了
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # 面积计算公式：栈顶元素的高度*（两边元素的索引-1），两边的索引都是第一个比当前元素小的索引。
                max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
            # 只有当前元素比栈顶元素大时才入栈，所以栈内元素都是从小到大进行排序的
            stack.append(i)
        return max_area

if __name__ == '__main__':
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(heights))
