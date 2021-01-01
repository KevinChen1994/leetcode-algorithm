# 排序

## 常考排序

### 快排

```python
class Solution:
    def quick_sort(self, nums, left, right):
        if left < right:
            pivot = self.partition(nums, left, right)
            self.quick_sort(nums, left, pivot - 1)
            self.quick_sort(nums, pivot + 1, right)

    def partition(self, nums, left, right):
        target = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[i] < target:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
```

### 归并排序

```python
class Solution:
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        l, r = 0, 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result
```

### 堆排序

```python
'''
solution: 先构建一个大顶推，大顶堆的定义是：每个节点的值都大于或等于他的左右孩子节点的值，也就是 Key[i] >= Key[2i+1] && Key[i] >= Key[2i+2]。另外堆是一个完全二叉树结构：假设一个二叉树的深度为h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。构建完成之后，将堆顶元素与堆的最下最右节点进行交换，然后再重新构建大顶堆，直到排序完成。
'''

class Solution:
    def heapify(self, nums, n, i):
        largest = i
        l = 2 * i + 1  # left = 2*i + 1  左子树
        r = 2 * i + 2  # right = 2*i + 2 右子树

        # 从左子树和右子树中选出最大的节点
        if l < n and nums[i] < nums[l]:
            largest = l

        if r < n and nums[largest] < nums[r]:
            largest = r

        # 如果最大的节点不是根节点，那么交换这两个节点，并继续进行调整
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]  # 交换
            self.heapify(nums, n, largest)

    def heapSort(self, nums):
        n = len(nums)

        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是n//2 -1 就是最后一个非叶子节点
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        # 将堆定元素与最下最右的元素进行交换
        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            # 重新构建大顶堆
            self.heapify(nums, i, 0)
```

