# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/14 23:42

class Solution:
    # DFS
    def numIslands_1(self, grid) -> int:
        return


if __name__ == '__main__':
    solution = Solution()
    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    print(solution.numIslands_1(grid))