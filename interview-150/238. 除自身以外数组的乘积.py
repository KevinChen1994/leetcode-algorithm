from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        L = [1] * len(nums)
        R = [1] * len(nums)
        for i in range(1, len(nums)):
            L[i] = L[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]
        for i in range(len(nums)):
            result.append(L[i] * R[i])
        return result
if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.productExceptSelf(nums))