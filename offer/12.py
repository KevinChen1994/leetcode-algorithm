# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/12 22:49

class Solution:
    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def exist(self, board, word) -> bool:
        self.m = len(board)
        if self.m == 0:
            return False
        self.n = len(board[0])
        self.board = board
        self.word = word
        self.marked = [[False for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(0, i, j):
                    return True
        return False

    def dfs(self, index, x, y):
        if index == len(self.word) - 1:
            return self.board[x][y] == self.word[index]
        if self.board[x][y] == self.word[index]:
            self.marked[x][y] = True
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < self.m and 0 <= new_y < self.n and not self.marked[new_x][new_y] and self.dfs(
                        index + 1, new_x, new_y):
                    return True
            self.marked[x][y] = False
        return False


if __name__ == '__main__':
    solution = Solution()
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(solution.exist(board, word))
