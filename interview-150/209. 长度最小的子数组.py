'''滑动窗口'''

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1  # 也可以写 inf
        s = left = 0
        for right, x in enumerate(nums):  # 枚举子数组右端点
            s += x
            while s >= target:  # 满足要求
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1  # 左端点右移
        return ans if ans <= n else 0



if __name__ == '__main__':
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))