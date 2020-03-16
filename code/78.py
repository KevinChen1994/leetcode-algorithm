# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/16 17:37
# software: PyCharm
'''
solution1: 回溯法。与迭代法思路相同。
solution2: 迭代。 每次遍历已有集合与当前遍历的字符相加
solution3: 使用itertools库
'''
class Solution:
    def subsets_1(self, nums):
        ans = []
        temp = []
        self.backtrack(nums, temp, ans, 0)
        return ans

    def backtrack(self, nums, temp, ans, i):
        ans.append(temp[:])
        for i in range(i, len(nums)):
            self.backtrack(nums, temp+[nums[i]], ans, i+1)

    # 迭代
    def subsets_2(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res

    def subsets_3(self,nums):
        import itertools
        res = []
        for i in range(len(nums) + 1):
            for tmp in itertools.combinations(nums, i):
                res.append(tmp)
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.subsets_3(nums))
