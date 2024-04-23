from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
            if num_dict[num] > len(nums) // 2:
                return num
    def majorityElement2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums) // 2]


if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement2(nums))