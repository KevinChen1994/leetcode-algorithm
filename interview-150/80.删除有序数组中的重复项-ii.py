from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start, end = 0, 1
        while end < len(nums):
            if nums[start] != nums[end]:
                if end - start > 2:
                    nums[start + 2:end] = [nums[end]] * (end - start - 2)
                start += 1
            end += 1
        return len(nums[:start+2])
            
    # 解决前K个一致的问题 
    def removeDuplicates2(self, nums: List[int]) -> int:
            def solve(k):
                u = 0
                for x in nums:
                    if u < k or nums[u - k] != x:
                        nums[u] = x
                        u += 1
                return u
            return solve(2)



if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,2,2,3]
    nums = [0,0,1,1,1,1,2,3,3]
    print(solution.removeDuplicates2(nums))