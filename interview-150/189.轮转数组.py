from typing import List

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 考虑k可能会比nums的长度大，这时候就进行循环旋转就行，具体做法是取余数，因为旋转数组的长度相当于没有旋转
        if k > len(nums):
            k = k % len(nums)
        if k == 0:
            return
        self.revserse(nums, 0, len(nums) - 1)
        self.revserse(nums, 0, k - 1)
        self.revserse(nums, k, len(nums) - 1)
    
    def revserse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 10
    print(solution.rotate(nums, k))