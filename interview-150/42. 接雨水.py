from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0
        left, right = 0, n - 1
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left < max_right:
                result += max(max_left - height[left], 0)
                left += 1
                max_left = max(max_left, height[left])
            else:
                result += max(max_right - height[right], 0)
                right -= 1
                max_right = max(max_right, height[right])
        return result

if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(solution.trap(height=height))