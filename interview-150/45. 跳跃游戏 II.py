from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        steps = 0
        end = 0
        for i in range(len(nums) - 1):
            max_reach = max(i + nums[i], max_reach)
            if i == end:
                end = max_reach
                steps += 1
        return steps


if __name__ == '__main__':
    solution = Solution()
    nums = [2,3,1,1,4]
    # nums = [2,1]
    print(solution.jump(nums))