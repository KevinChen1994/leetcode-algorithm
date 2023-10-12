# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/6 15:02
from typing import List
'''
solution: 跟leetcode-54思想一样，反着来就行了。
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        flag = 0
        for num in range(1, n * n + 1):
            result[i][j] = num
            i_tmp = i + directions[flag][0]
            j_tmp = j + directions[flag][1]
            if 0 <= i_tmp < n and 0 <= j_tmp < n and result[i_tmp][j_tmp] == 0:
                i, j = i_tmp, j_tmp
            else:
                flag = (flag + 1) % len(directions)
                i += directions[flag][0]
                j += directions[flag][1]
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.generateMatrix(n))
