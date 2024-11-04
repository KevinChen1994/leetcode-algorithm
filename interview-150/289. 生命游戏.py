from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for x in range(max(0, i-1), min(m, i+2)):
                    for y in range(max(0, j-1), min(n, j+2)):
                        count += board[x][y] & 1
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
        print(board)

if __name__ == '__main__':
    solution = Solution()
    solution.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])  # [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        