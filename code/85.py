# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/18 21:46
# software: PyCharm
'''
solution1: 动态规划，使用柱状图优化暴力法。在dp数组中记录以每个位置为终点的最大长度，计算面积时，以(i,j)为右下角，从下往上遍历，
先计算最小的宽，通过宽乘(当前行-遍历到的行+1)计算面积。
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

            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[i], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                ans = max(ans, height[j] * (right[j] - left[j]))
        return ans


if __name__ == '__main__':
    solution = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(solution.maximalRectangle_2(matrix))
