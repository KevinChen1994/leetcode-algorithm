# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/2/4 13:37
from typing import List
'''
solution: 官方题解中使用的是将nums1的前m个复制到另外一个数组中，然后合并在赋值给nums1，这种方法虽然简单，
但是我总感觉脱离了这道题要考察的点，因为没有在原nums1上进行操作。
我们使用双指针来解决，分别指向nums1的第m-1个和nums2的第n-1个，记录nums1的总长度为m+n，逐一判断nums1和nums2最后一个元素，
哪个大就移动到nums1的最后一个位置，至于为什么要讲n和m分别用while来判断，是因为有一个数据是这样的
nums1 = [0]，m = 0，nums2 = [1]，n = 1。很恶心的是，m给的是0，如果m和n同时判断的话，nums2的值就没办法复制到nums1中。
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = m + n - 1
        m -= 1
        n -= 1
        while n >= 0:
            while m >= 0 and nums1[m] >= nums2[n]:
                nums1[l] = nums1[m]
                l -= 1
                m -= 1
            nums1[l] = nums2[n]
            n -= 1
            l -= 1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)
