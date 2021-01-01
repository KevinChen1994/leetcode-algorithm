# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/12/30 10:44
'''
solution: 需要分情况讨论：
1. 当子串首尾相同时：
1.1 去掉首尾后的子串不包含首尾的字符
count('bccb') = 2 * count('cc') + 2 = 2 * 2 + 2 = 6 -> c cc bcb bccb b bb
（相当于cc的解在前后分别加上b，那么这个就是cc解的两倍，另外在加上bb的解，也就是b和bb，也就是2）
count('cc') = 2 * count('') + 2 = 2 -> c cc
1.2 去掉首尾的子串后包含一个首尾的字符
count('bcbcb') = 2 * count('cbc') + 1 = 2 * 4 + 1 = 9
（cbc的解为b cbc c cc，按照1.1的方法会得出b cbc c cc bbb bcbcb bcb bccb b bb，可以看到有两个重复的b，
原因就是去掉首尾的子串中包含首尾的字符，所以子串中的那个字符单独作为一个子串的时候会与首尾字符单独作为子串的时候重复。
所以1.1公式就不适用了，需要将最后的+2改成+1，去掉重复的一个子串。）
count('cbc') = 2 * count('b') + 2 = 4
1.3 去掉首尾的子串包含两个或两个以上首尾字符
count('bbcabb') = 2 * count('bcab') - count('ca') = 2 * 6 - 2 = 10
（bcab的解为c a bcb bab b bb，如果按照1.1的方法会的出c a bcb bab b bb bcb bab bbcbb bbabb bbb bbbb b bb，
可以看到有四个重复子串bcb bab b bb，出现这几个重复的解的原因就是ca的子串与里边的bb计算了一次，与外边的bb又计算了一次，
所以我们需要去掉一部分，我们将ca的解减去就是正确的答案。）
count('bcab') = 2 * count('ca') + 2 = 6
2. 当子串首尾不同时：
count('abcc') = count('abc') + count('bcc') - count('bc') = 4
count('abc') = count('ab') + count('bc') - count('b') = 3
count('bcc') = count('bc') + count('cc') - count('c') = 3
count('bc') = 2
这个很好理解，相当于将问题进行拆分，先计算去掉最后一个字符后的子串，在计算去掉第一个字符的子串，因为中间字符的子串重复计算了，所以减去。
3. base case：
count('a') = 1
count('') = 0
'''


class Solution:
    # 带记忆的递归
    def countPalindromicSubsequences(self, S: str) -> int:
        n = len(S)
        self.memo = [[None for _ in range(n)] for _ in range(n)]
        return self.count(S, 0, n - 1)

    def count(self, S, i, j):
        if i > j:
            return 0
        if i == j:
            return 1
        if self.memo[i][j]:
            return self.memo[i][j]
        if S[i] == S[j]:
            ans = 2 * self.count(S, i + 1, j - 1)
            l = i + 1
            r = j - 1
            while l <= r and S[l] != S[i]:
                l += 1
            while l <= r and S[r] != S[i]:
                r -= 1
            if l > r:  # 1.1
                ans += 2
            elif l == r:  # 1.2
                ans += 1
            else:  # 1.3
                ans -= self.count(S, l + 1, r - 1)
        else:  # 2
            ans = self.count(S, i, j - 1) + self.count(S, i + 1, j) - self.count(S, i + 1, j - 1)
        self.memo[i][j] = ans % 1000000007
        return self.memo[i][j]

    # dp
    def countPalindromicSubsequences_2(self, S):
        n = len(S)
        if n == 0:
            return 0
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for size in range(1, n + 1):
            for i in range(n - size):
                j = i + size
                if S[i] == S[j]:
                    dp[i][j] = 2 * dp[i + 1][j - 1]
                    l = i + 1
                    r = j - 1
                    while l <= r and S[l] != S[i]:
                        l += 1
                    while l <= r and S[r] != S[i]:
                        r -= 1
                    if l > r:
                        dp[i][j] += 2
                    elif l == r:
                        dp[i][j] += 1
                    else:
                        dp[i][j] -= dp[l + 1][r - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                dp[i][j] %= 1000000007
        return dp[0][n - 1]


if __name__ == '__main__':
    solution = Solution()
    S = 'bccb'
    print(solution.countPalindromicSubsequences_2(S))
