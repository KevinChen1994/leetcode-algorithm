# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/24 20:19

class Solution:
    def minNumber(self, nums) -> str:
        num_str = [str(num) for num in nums]
        self.quick_sort(num_str, 0, len(num_str) - 1)
        return ''.join(num_str)

    def quick_sort(self, nums_str, left, right):
        i, j = left, right
        if left < right:
            # 这里采用快排的思想
            while i < j:
                # j在右边，如果j在left左边大于等于j在left的右边，满足要求。此时要的就是j在left右边比较小
                while nums_str[j] + nums_str[left] >= nums_str[left] + nums_str[j] and i < j:
                    j -= 1
                # 同理。i在左边，如果i在left的左边小于等于i在left的右边，满足要求。此时要的就是i在left左边比较小。
                while nums_str[i] + nums_str[left] <= nums_str[left] + nums_str[i] and i < j:
                    i += 1
                # 此时如果i != j，那么这两个值都是不符合要求的，进行交换顺序继续进行排序。
                nums_str[i], nums_str[j] = nums_str[j], nums_str[i]
            # 此时，i左边所有的元素，在left的左边都比在left的右边要小；i右边的所有元素，在left的左边都比在left的右边要大。
            # 所以i这个位置就固定了，并与left位置的元素进行交换，之后去排序i左边的和右边所有元素即可。
            nums_str[i], nums_str[left] = nums_str[left], nums_str[i]
            self.quick_sort(nums_str, left, i - 1)
            self.quick_sort(nums_str, i + 1, right)


if __name__ == '__main__':
    solution = Solution()
    # nums = [1, 4, 7, 2, 5, 8, 0, 3, 6, 9]
    nums = [1, 4, 2, 0, 3]
    print(solution.minNumber(nums))
