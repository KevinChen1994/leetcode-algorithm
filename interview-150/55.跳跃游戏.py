from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_position = 0
        for i, num in enumerate(nums):
            if i > max_position:
                return False
            max_position = max(max_position, i + num)
            if max_position >= len(nums) - 1:
                return True
        return True



if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    print(solution.canJump(nums))