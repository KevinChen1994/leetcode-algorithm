# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/22 22:26
'''
solution1: 使用堆排序
solution2: 使用快排思想
'''
class Solution:
    def getLeastNumbers_1(self, arr, k: int):
        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr[:k]

    def heapify(self, nums, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and nums[largest] < nums[left]:
            largest = left
        if right < n and nums[largest] < nums[right]:
            largest = right
        if i != largest:
            nums[i], nums[largest] = nums[largest], nums[i]
            self.heapify(nums, n, largest)

    def getLeastNumbers_2(self, arr, k):
        if k == 0 or len(arr) == 0:
            return []
        # 前k个数，下标就是k - 1
        return self.quick_search(arr, 0, len(arr) - 1, k - 1)

    def quick_search(self, nums, left, right, k):
        povit = self.partition(nums, left, right)
        # 如果当前排序元素索引与k相同，那么直接返回
        if povit == k:
            return nums[:k + 1]
        # 根据当前元素索引与k的大小决定继续排序哪一边
        if povit > k:
            return self.quick_search(nums, left, povit - 1, k)
        else:
            return self.quick_search(nums, povit + 1, right, k)

    def partition(self, nums, left, right):
        i = left - 1
        target = nums[right]
        for j in range(left, right):
            if nums[j] < target:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    arr = [3, 2, 1,5,3,1,7]
    k = 2
    print(solution.getLeastNumbers_2(arr, k))
