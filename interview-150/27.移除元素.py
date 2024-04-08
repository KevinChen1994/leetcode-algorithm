from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[end] == val:
                end -= 1
            elif nums[start] == val:
                nums[start], nums[end] = nums[end], val
                start += 1
                end -= 1
            else:
                start += 1
        return start
if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    print(solution.removeElement(nums, val))
                


