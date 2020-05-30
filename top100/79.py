# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/16 22:30
# software: PyCharm
'''
solution: DFS+状态重置，思路很简单，实现起来费劲 -,-|||
'''


class Solution:
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def search_word(self, board, word, index, x, y, marked, m, n):
        if index == len(word) - 1:
            return board[x][y] == word[index]

        if board[x][y] == word[index]:
            marked[x][y] = True
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] \
                        and self.search_word(board, word, index + 1, new_x, new_y, marked, m, n):
                    return True
            # 如果四个方向都不符合要求，那么这里就重置为False，以便从其他位置访问到这里
            marked[x][y] = False
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCCED'
    # word = 'SEE'
    print(solution.exist(board, word))
