from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left, right = [1] * n, [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        count = left[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            count += max(left[i], right[i])
        return count
            


if __name__ == '__main__':
    solution = Solution()
    ratings = [1,0,2]
    ratings = [1,2,2]
    # ratings = [1,2,3,3,2]
    print(solution.candy(ratings))