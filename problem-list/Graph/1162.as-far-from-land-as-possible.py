# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 23:32
from typing import List
'''
solution: 这道题我拿到手第一反应还是dfs，先找到每个陆地，然后将陆地所有的坐标按照陆地编号保存起来，
然后遍历每个海洋，逐步找到最远的海洋，结果超时了，因为找陆地时间复杂度是O(n²)，找海洋时间复杂度也是O(n²)，
但是找到海洋后，还要去遍历陆地的索引，这就导致了时间复杂度又上升了一个维度，变成了接近O(n_3)。
看了题解才明白过来，这是典型的BFS类型题目。BFS与DFS不同的是，DFS是一条路走到底，比如一个节点，他会沿着他一直往下搜索，一直到结束；
BFS是一层一层的搜索，先找到的一定是最近的，后找到的一定是最远的。利用这个性质，我们使用BFS最后找到海洋一定是最远的海洋。

'''

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        # 如果全是陆地或者全是海洋
        if len(queue) == m * n or len(queue) == 0:
            return -1
        # 使用BFS进行遍历，最后遍历到的就是最远的海洋
        while queue:
            cur_i, cur_j = queue.pop(0)
            for direction in directions:
                new_i, new_j = cur_i + direction[0], cur_j + direction[1]
                if new_i < 0 or new_j < 0 or new_i >= m or new_j >= n or grid[new_i][new_j] != 0:
                    continue
                # 在原矩阵进行修改，每次都是当前值加1
                grid[new_i][new_j] = grid[cur_i][cur_j] + 1
                queue.append((new_i, new_j))
        # 因为陆地的初始值是1，所以用最远的海洋距离减1
        return grid[cur_i][cur_j] - 1


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print(solution.maxDistance(grid))
