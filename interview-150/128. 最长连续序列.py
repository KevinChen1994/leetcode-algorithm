from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_res = 0
        for num in nums:
            if num - 1 not in nums:
                cur_num = num
                cur_res = 1
                while cur_num + 1 in nums:
                    cur_num += 1
                    cur_res += 1
                max_res = max(max_res, cur_res)
        return max_res
            
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))  # 4