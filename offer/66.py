# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/23 17:49
'''
solution: 可以将数组变成一个二维数组，横坐标与纵坐标都相等，让对角线变成1，因为想要的结果是当前行不包含当前元素的乘积，
依次计算下三角和上三角，对应的横坐标相乘即可。
'''
class Solution:
    def constructArr(self, a):
        res = [1] * len(a)
        tmp = 1
        # 计算下三角
        for i in range(1, len(a)):
            res[i] = res[i - 1] * a[i - 1]
        # 计算下三角
        for i in range(len(a) - 2, -1, -1):
            tmp *= a[i + 1]
            res[i] *= tmp
        return res


solution = Solution()
a = [2, 3, 4, 5]
print(solution.constructArr(a))
