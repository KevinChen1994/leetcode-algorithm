from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x, y, left):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0:
                return 0
            if grid[x][y] == 2:
                return left == 0
            grid[x][y] = -1
            ans = (
                dfs(x - 1, y, left - 1)
                + dfs(x + 1, y, left - 1)
                + dfs(x, y - 1, left - 1)
                + dfs(x, y + 1, left - 1)
            )
            grid[x][y] = 0 # 恢复现场
            return ans
        
        cnt0 = sum(row.count(0) for row in grid)
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1:
                    return dfs(i, j, cnt0 + 1) # 算上起点
                


if __name__ == '__main__':
    solution = Solution()
    grid = [
        [1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]
        ]
#     1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
#     2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
    print(solution.uniquePathsIII(grid))
    