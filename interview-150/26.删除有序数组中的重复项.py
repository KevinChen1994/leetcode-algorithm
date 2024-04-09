from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 1
        while end < len(nums):
            if nums[start] != nums[end]:
                nums[start + 1] = nums[end]
                start += 1
            end += 1
        return len(nums[:start + 1])

if __name__ == '__main__':
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))