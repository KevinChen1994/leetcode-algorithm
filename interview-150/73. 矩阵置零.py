from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        index_list = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    index_list.append((i, j))
        for index in index_list:
            matrix[index[0]] = [0] * n
            for i in range(m):
                matrix[i][index[1]] = 0
        print(matrix)
    
    # 空间复杂度为O(1)的方法，使用第一行和第一列来存储是否有0
    def setZeroes_(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row and first column to mark zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set matrix cells to zero based on marks
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Set first row to zero if needed
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Set first column to zero if needed
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == '__main__':
    solution = Solution()
    # solution.setZeroes( [
    #                             [0,1,2,0],
    #                             [3,4,5,2],
    #                             [1,3,1,5]
    #                             ])
    solution.setZeroes( [
                                [1,1,1],
                                [1,0,1],
                                [1,1,1]
                                ])

