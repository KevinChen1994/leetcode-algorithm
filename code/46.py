# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/4 15:50
# software: PyCharm

'''
回溯算法框架。其核心就是 for 循环里面的递归，在递归调用之前「做选择」，在递归调用之后「撤销选择」
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''


class Solution:
    def permute(self, nums):
        ans = []
        tmp = []
        self.backtrack(nums, tmp, ans)
        return ans

    def backtrack(self, nums, tmp, ans):
        if not nums:
            # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
            # 或者使用 tmp.copy()
            ans.append(tmp[:])
            return
        for i in range(len(nums)):
            tmp.append(nums[i])
            # nums为除去添加到tmp中的其他值
            self.backtrack(nums[:i] + nums[i + 1:], tmp, ans)
            tmp.pop()


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.permute(nums))
