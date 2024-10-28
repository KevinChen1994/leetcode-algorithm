from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 先转置矩阵
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        # 再翻转每一行
        for i in range(n):
            matrix[i].reverse()
        print(matrix)

if __name__ == '__main__':
    solution = Solution()
    solution.rotate([
                            [1,2,3],
                            [4,5,6],
                            [7,8,9]]) 
                        # [[7,4,1],
                        # [8,5,2],
                        # [9,6,3]]
                        # 0,0 -> 0,2 0,2 -> 2,2 2,2 -> 2,0 2,0 -> 0,0
                        # 0,1 -> 1,2 1,2 -> 2,1 2,1 -> 1,0 1,0 -> 0,1