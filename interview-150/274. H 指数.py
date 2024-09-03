from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        n = len(citations)
        citations = sorted(citations)
        for i in range(n):
            if citations[i] >= n - i:
                res = n - i
                break
        return res

if __name__ == '__main__':
    solution = Solution()
    citations = [3,0,6,1,5]
    print(solution.hIndex(citations))