# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/14 23:42
'''
solution1: DFS。设置一个marked的状态矩阵，在遍历的过程中，设定四个方向，上下左右移动，进行深度优先遍历，如果遇到1，marked改成True，直到所有连接的岛屿都被找到，
进行下一个位置的遍历。
solution2: BFS。与DFS累死，没有使用递归，借用队列实现。
solution3: 合并连接的岛屿，代码看的不是很明白。参考https://leetcode-cn.com/problems/number-of-islands/solution/dfs-bfs-bing-cha-ji-python-dai-ma-java-dai-ma-by-l/
'''
from _collections import deque


class Solution_1:
    #        x-1,y
    # x,y-1    x,y      x,y+1
    #        x+1,y
    # 方向数组，它表示了相对于当前位置的 4 个方向的横、纵坐标的偏移量，这是一个常见的技巧
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def numIslands(self, grid) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n, marked)

        return count

    def dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] and grid[new_i][new_j] == '1':
                self.dfs(grid, new_i, new_j, m, n, marked)


class Solution_2:
    directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def numIslands(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0
        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    while queue:
                        cur_i, cur_j = queue.popleft()
                        for direction in self.directions:
                            new_i = cur_i + direction[0]
                            new_j = cur_j + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1' and not marked[new_i][
                                new_j]:
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count


class Solution_3:
    def numIslands(self, grid):

        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def is_connected(self, p, q):
                return self.find(p) == self.find(q)

            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return

                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1

                self.count -= 1

        row = len(grid)
        # 特判
        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y

        # 注意：我们不用像 DFS 和 BFS 一样，4 个方向都要尝试，只要看一看右边和下面就可以了
        directions = [(1, 0), (0, 1)]
        # 多开一个空间，把水域 "0" 都归到这个虚拟的老大上
        dummy_node = row * col

        # 多开的一个空间就是那个虚拟的空间
        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                # 如果是水域，都连到那个虚拟的空间去
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    # 向下向右如果都是陆地，即 "1"，就要合并一下
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        # 不要忘记把那个虚拟结点减掉
        return uf.get_count() - 1


if __name__ == '__main__':
    solution = Solution_3()
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    print(solution.numIslands(grid))
