# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/16 23:06
'''
solution1: 用0去找1，首先将全部0的坐标入队，然后将所有1改为-1。在遍历队列过程中，用0的坐标分别从上下左右四个方向去找-1，如果找到的话就在原矩阵的基础上用0位置的值加1赋值到新的位置，并将新的位置入队，因为这个位置可以间接去找到其他没有挨着0的1.
solution2: 先找到所有挨着0的1，将这些位置入队，并将对应的result矩阵改为1，因为他们挨着0，所以距离为1；然后用这些1去找没有挨着0的1，找到后用原始位置的值加上1就是找到位置与0之间的距离。
solution3: 动态规划。定义动态转移矩阵:$$ dp(i,j) = \begin{cases} 1 + min(dp[i-1][j], dp[i+1][j],dp[i][j-1],dp[i][j+1]) & \text{matrix[i][j] == 1}\\ 0& \text{matrix[i][j] == 0} \end{cases}$$
用dp[i][j]表示距离0的最近位置，但是发现dp[i][j]是由其上下左右四个方向的状态决定的，没办法从一个方向开始递推。于是从四个角开始递推，最终整个的结果就是最终的结果。
'''


class Solution:
    def updateMatrix_1(self, matrix):
        queue = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i, j))
                else:
                    matrix[i][j] = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.pop(0)
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == -1:
                    matrix[new_x][new_y] = matrix[x][y] + 1
                    queue.append((new_x, new_y))

        return matrix

    def updateMatrix_2(self, matrix):
        queue = []
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for i in range(n)] for j in range(m)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # 先找到矩阵中的挨着0的1，将他们的坐标放到队列中
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for direction in directions:
                        x = i + direction[0]
                        y = j + direction[1]
                        if 0 <= x < m and 0 <= y < n and matrix[x][y] == 1 and result[x][y] == 0:
                            # 这个1是挨着0的1，将result直接赋值为1；防止重复入队；
                            result[x][y] = 1
                            queue.append((x, y))
        while queue:
            x, y = queue.pop(0)
            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                # 这里是找到挨着1的1
                if 0 <= new_x < m and 0 <= new_y < n and matrix[new_x][new_y] == 1 and result[new_x][new_y] == 0:
                    result[new_x][new_y] = result[x][y] + 1
                    queue.append((new_x, new_y))
        return result

    def updateMatrix_3(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = matrix[i][j] if matrix[i][j] == 0 else float('inf')
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j + 1 < n:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
        return dp


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    # matrix = [[0], [0], [0], [0], [0]]
    print(solution.updateMatrix_3(matrix))
