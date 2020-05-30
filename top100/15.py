# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/15 13:29
# software: PyCharm

class Solution:
    # 双指针方法
    def threeSum(self, nums):
        n = len(nums)
        result = []
        # 如果长度小于3或者为空，直接返回空
        if not nums or n < 3:
            return result
        # 将列表排序
        nums.sort()
        for i in range(n):
            # 当前元素为大于0的数，那么后边全是大于0的数，相加不可能为0，直接返回结果
            if nums[i] > 0:
                return result
            # 对于重复元素，要跳过，避免重复解，例如：[-1,-1,0,1]，如果不挑过，会出现两次[-1,0,1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 如果左指针指向的元素与左指针右边的元素相等，那么移动左指针，避免出现重复解，例如[-2,1,1,1,1,1]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.a([-1, 0, 1, 2, -1, -4]))
