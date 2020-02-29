# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/29 20:20
# software: PyCharm

'''
给定的数组因为之前是按照从小到大排序的，然后以其中一个元素为轴进行了旋转
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
那么就可以通过mid索引元素与头尾元素大小比较得出来，哪一段是有序的。
之后就可以通过二分查找进行搜索。
时间复杂度为logn，因为在二分查找下查找元素个数n/2、n/4、n/8...1，假设需要查找x次，最坏情况为查到只剩一个元素
n/2^x=1,==> x=logn
'''
class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            # mid 之前的元素是从小到大排序的
            if nums[mid] > nums[end]:
                # target 在前半部分
                if target >= nums[start] and target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            # mid 之后的元素是从小到大排序的
            else:
                # target 在后半部分
                if target >= nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    print(solution.search(nums, target))
