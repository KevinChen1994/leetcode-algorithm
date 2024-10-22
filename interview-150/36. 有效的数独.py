'''考察的是对矩阵的遍历？'''

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])
        for i in range(row):
            row_set = set()
            col_set = set()
            for j in range(col):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
        for i in range(0, row, 3):
            for j in range(0, col, 3):
                sub_set = set()
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] in sub_set:
                                return False
                            sub_set.add(board[i+m][j+n])
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."]
                                        ,["6",".",".","1","9","5",".",".","."]
                                        ,[".","9","8",".",".",".",".","6","."]
                                        ,["8",".",".",".","6",".",".",".","3"]
                                        ,["4",".",".","8",".","3",".",".","1"]
                                        ,["7",".",".",".","2",".",".",".","6"]
                                        ,[".","6",".",".",".",".","2","8","."]
                                        ,[".",".",".","4","1","9",".",".","5"]
                                        ,[".",".",".",".","8",".",".","7","9"]]))