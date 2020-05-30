# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/18 21:46
# software: PyCharm
'''
solution1: 动态规划，使用柱状图优化暴力法。在dp数组中记录以每个位置为终点的最大长度，计算面积时，以(i,j)为右下角，从下往上遍历，
先计算最小的宽，通过宽乘(当前行-遍历到的行+1)计算面积。
solution2: 动态规划，计算每个点的最大高度，在计算这个最大高度的左边界与右边界。通过遍历一层一层计算高与左边界和右边界。
每层的值都依赖于上一层的值与当前矩阵的值。思路很好，但是左边界与右边界不太容易理解。
solution3: 栈。通过动态规划，计算每一行的最大高度，然后将高度传给84题，直接得出结果。-，-||| 就是这么简单粗暴。
'''


class Solution:
    # 动态规划，超时。
    def maximalRectangle_1(self, matrix):
        ans = 0
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                # 动态记录以（i,j）为最终点的长度，存储在dp中
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1
                # 从当前行往上找，找到每行以（i,j）为右下角的最小长度，用长度乘高度（当前行-遍历到的行+1）
                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    ans = max(ans, width * (i - k + 1))
        return ans

    # 动态规划
    def maximalRectangle_2(self, matrix):
        ans = 0
        m = len(matrix)
        if m == 0:
            return ans
        n = len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        for i in range(m):
            cur_left, cur_right = 0, n

            # 更新当前点最大高度，如果是1，那么就在上一个点的高度上加1，否则是0
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # 更新当前点最大左边坐标，
            for j in range(n):
                if matrix[i][j] == '1':
                    # 比较上一行的左边界与当前行的左边界，较大的作为当前左边界，因为较大的那行左边是包含0的，这样在这一列上就不能构成矩形
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    # 当前点的左边界为0，下一个点的边界从j+1开始
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    # 与计算左边界思路一样，相反就是右边界
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                ans = max(ans, height[j] * (right[j] - left[j]))
        return ans

    def maximalRectangle_3(self, matrix):
        if not matrix: return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            # 计算每一行的最大高度，将高度传给84题，直接计算面积。
            maxarea = max(maxarea, self.test(dp))
        return maxarea

    def leetcode84(self, heights):
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
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle_3(matrix))
