from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        def calculate(boxes, l, r, k):
            if (l > r):
                return 0
            if dp[l][r][k] == 0:
                r1, k1 = r, k
                while r1 > l and boxes[r1] == boxes[r1 - 1]:
                    r1 -= 1
                    k1 += 1
                dp[l][r][k] = calculate(boxes, l, r1 - 1, 0) + (k1 + 1) * (k1 + 1)
                for i in range(l, r1):
                    if boxes[i] == boxes[r1]:
                        dp[l][r][k] = max(dp[l][r][k], calculate(boxes, l, i, k1 + 1) + calculate(boxes, i + 1, r1 - 1, 0))
            return dp[l][r][k]
        return calculate(boxes, 0, n - 1, 0)
    
if __name__ == '__main__':
    solution = Solution()
    boxes = [1,3,2,2,2,3,4,3,1]
    res = solution.removeBoxes(boxes)
    print(res)