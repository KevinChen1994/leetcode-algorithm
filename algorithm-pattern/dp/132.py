# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/23 15:29

class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        # 这里借鉴了第5题的思路，使用动态规划在判断是否为回文
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点，如果s[0:i]不是回文，那么从s[1:i]开始进行判断，如果是回文就在那个位置的需要切割的次数加1，
            # 最终去最小值就是这个序列需要切割的最小值
            for j in range(i):
                # check_palindrome[j + 1][i]的原因是j在这个循环中取不到i的值，所以就忽略了单个值的情况；
                # 另外j=0的时候已经在上边判断过了，这里无需在判断。
                if check_palindrome[j + 1][i]:
                    dp[i] = min(dp[j] + 1, dp[i])

        return dp[size - 1]


if __name__ == '__main__':
    solution = Solution()
    s = "abaaba"
    print(solution.minCut(s))
