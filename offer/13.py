# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/17 22:27
'''
solution: 使用dfs或者bfs都可以，机器人按照当前坐标，只能移动一个格，所以不能遍历所有的位置来判断是否符合要求，
当机器人遇到一个不符合要求的位置的时候，那后边的位置肯定也是不符合要求的。
这道题的难点在于如何求位数和，其实可以使用一个比较笨的方法：
def sum(x):
    s = 0
    while x != 0:
        s = x % 10
        x = x // 10
    return s
但是由于机器人每次只移动一个格，所以位数和是有一定的规律的：
数位和增量公式： 设 x 的数位和为 s_x，x+1 的数位和为 s_{x+1}
1 当 (x+1)%10=0时，s_{x+1}=s_x-8，例如：19,20 的数位和分别为 10, 2；
2 当 (x+1)%10!=0时，s_{x+1}=s_x+1，例如：1, 2的数位和分别为 1, 2。
'''


class Solution:
    def movingCount_1(self, m: int, n: int, k: int) -> int:
        # i,j是当前索引，si,sj是位数和
        def dfs(i, j, si, sj):
            if i >= m or j >= n or si + sj > k or (i, j) in visited:
                return 0
            visited.add((i, j))
            return 1 + dfs(i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj) + dfs(i, j + 1, si,
                                                                                   sj + 1 if (j + 1) % 10 else sj - 8)

        visited = set()
        return dfs(0, 0, 0, 0)

    def movingCount_2(self, m, n, k):
        queue, visited = [(0, 0, 0, 0)], set()
        while queue:
            i, j, si, sj = queue.pop(0)
            if i >= m or j >= n or k < si + sj or (i, j) in visited:
                continue
            visited.add((i, j))
            queue.append((i + 1, j, si + 1 if (i + 1) % 10 else si - 8, sj))
            queue.append((i, j + 1, si, sj + 1 if (j + 1) % 10 else sj - 8))
        return len(visited)


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 2
    k = 17
    print(solution.movingCount_2(m, n, k))
