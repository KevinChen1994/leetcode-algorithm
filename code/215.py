# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/19 21:00
'''
solution1: 排序好，返回第k-1个元素
solution2: 动态创建一个大顶堆，并保持堆的大小小于等于k，这样，堆就保留了前k个最大的元素，堆定元素就是答案
solution3: 思路类似于快排，题目想要找的是第k个大的数，那么快排的过程是选中一个分界元素，将比他小的元素移动到分界元素的左边，比他大的元素移动到分界元素右边，
那么一趟下来分界元素的位置就确定了。现在需要做的就是对比分界元素的位置与题目要求的k的大小，第K的元素，也就是第(n-k)小的元素，分界元素的索引与n-k相同的话，这就是答案。
'''

import heapq
import random


class Solution:
    def findKthLargest_1(self, nums, k) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest_2(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest_3(self, nums, k):

        def partition(left, right, pivot_index):
            # 确定轴
            pivot = nums[pivot_index]
            # 将轴元素移动到最后
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            # 将比轴元素小的数移动到左边
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def select(left, right, k_smallest):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return select(left, pivot_index - 1, k_smallest)
            else:
                return select(pivot_index + 1, right, k_smallest)

        return select(0, len(nums) - 1, len(nums) - k)


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    nums = [3, 2, 1, 5, 6, 4]
    k = 4
    k = 2
    print(solution.findKthLargest_3(nums, k))
