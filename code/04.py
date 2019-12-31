# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2019/12/31 16:53
# software: PyCharm

'''
自己实现的将两个有序的列表合并成一个有序的列表
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        i = j = 0
        nums = []
        while len(nums1) >= i + 1 and len(nums2) >= j + 1:
            if nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i += 1
        if i + 1 <= len(nums1):
            nums += nums1[i:]
        if j + 1 <= len(nums2):
            nums += nums2[j:]
        len_num = len(nums)
        if len_num % 2 == 1:
            return nums[len_num // 2]
        else:
            return (nums[len_num // 2 - 1] + nums[len_num // 2]) / 2


'''
使用Python内置函数sorted将两个有序的列表合并成一个有序的列表，事实证明官方的比我的快一点....
//求两数相除的整数商比/求两数相除的浮点型的商要耗费时间，尽量使用/然后用过int转一下。
另外len(nums)好像也是耗费时间的，能少用一次就少用一次吧。相同的代码提交了几次结果时间不同，让我有点不懂。
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        if len(nums) % 2 == 1:
            return nums[int(len(nums) / 2)]
        else:
            n = int(len(nums) / 2)
            return (nums[n - 1] + nums[n]) / 2

if __name__ == '__main__':
    solution = Solution()
    num1 = [1, 2]
    num2 = [3]
    print(solution.findMedianSortedArrays(num1, num2))
