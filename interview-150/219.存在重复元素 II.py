from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_dict = {}
        for index, num in enumerate(nums):
            if num in num_dict:
                if index - num_dict[num] <= k:
                    return True
                else:
                    num_dict[num] = index
            else:
                num_dict[num] = index
        return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums=[1,2,3,1], k=3))  # True