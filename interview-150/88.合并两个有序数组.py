from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[index] = nums1[m - 1]
                m -= 1
                index -= 1
            else:
                nums1[index] = nums2[n - 1]
                index -= 1
                n -= 1
        nums1[:n] = nums2[:n]




if __name__ == '__main__':
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)