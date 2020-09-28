# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/28 13:42
'''
solution1: 一共有n个数字，x1 x2 x3 ... xi-2 xi-1 xi ... xn，假设x1 x2 .. xi-2一共有f(i-2)种翻译，x1 x2 .. xi-2 xi-1一共有f(i-1)种翻译；
当整体翻译xi-1 xi时，x1 x2 .. xi-2 xi-1 xi一共有f(i-2)种翻译，因为xi-1 xi是固定的，所以翻译个数为f(i-2)；
当单独翻译xi时，x1 x2 .. xi-2 xi-1 xi一共有f(i-1)种翻译，因为xi是固定的，所以翻译个数为f(i-1)。
则可得出dp动态转移矩阵：dp(i) = dp(i-2) + dp(i-1)，当xi-1 xi可被一起翻译时； dp(i) = dp(i-1)，当xi-1 xi不可被一起翻译时。
判断xi-1 xi是否可以一起翻译，只需要判断xi-1 xi组成的数字是否大于等于10和小于等于25即可，（考虑到xi-1是0的情况）。
默认dp[0] = dp[1] = 1
solution2: 不适用动态转移矩阵，适用两个变量存储dp[i-2] 和dp[i-1]节省空间。
'''
class Solution:
    def translateNum_1(self, num: int) -> int:
        num_str = str(num)
        dp = [0] * (len(num_str) + 1)
        dp[0] = dp[1] = 1
        for i in range(2, len(num_str) + 1):
            if 10 <= int(num_str[i - 2:i]) <= 25:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

    def translateNum_2(self, num):
        num_str = str(num)
        a = b = 1
        for i in range(2, len(num_str) + 1):
            a, b = (a + b if 10 <= int(num_str[i-2:i]) <= 25 else a), a
        return a

if __name__ == '__main__':
    solution = Solution()
    num = 12258
    print(solution.translateNum_2(num))
