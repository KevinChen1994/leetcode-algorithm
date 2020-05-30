# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/13 13:59
# software: PyCharm

class Solution:
    '''
    暴力法 O(n3)
    '''
    def longestPalindrome_1(self, s):
        max = 0
        ans = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.isPalindrome(s[i:j]) and len(s[i:j]) > max:
                    ans = s[i:j]
                    max = len(ans)
        return ans

    def isPalindrome(self, s):
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    '''
    时间：108 ms 空间：13.3 MB
    '''
    def longestPalindrome_2(self, s):
        # 使用动态规划，用空间换时间，把问题拆分
        # 获取字符串s的长度
        str_length = len(s)
        # 记录最大字符串长度
        max_length = 0
        # 记录位置
        start = 0
        # 循环遍历字符串的每一个字符
        for i in range(str_length):
            # 当前回文字符串往前减1和往后加1，是否还是回文字符串
            if i - max_length >= 1 and s[i - max_length - 1: i + 1] == s[i - max_length - 1: i + 1][::-1]:
                # 记录当前开始位置
                start = i - max_length - 1
                # 取字符串最小长度为2，所以+=2，s[i-max_length-1: i+1]
                max_length += 2
                continue
            # 当前回文字符串往后加1，是否还是回文字符串
            if i - max_length >= 0 and s[i - max_length: i + 1] == s[i - max_length: i + 1][::-1]:
                start = i - max_length
                # 取字符串最小长度为1，所以+=1，s[i-max_length: i+1]
                max_length += 1
        return s[start: start + max_length]

    '''
    时间：752 ms 空间：13.3 MB
    '''
    def longestPalindrome_3(self, s):
        n = len(s)

        # 计算以l和r为中心的最大的回文字符串的长度
        def getLen(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        start = 0
        length = 0
        for i in range(n):
            cur = max(getLen(i, i), getLen(i, i + 1))
            if cur <= length: continue
            length = cur
            start = i - (cur - 1) // 2
        return s[start: start + length]

    '''
    很经典的动态规划解法，使用状态转移矩阵。
    '''
    def longestPalindrome_4(self, s):
        size = len(s)
        if size < 2:
            return s

        dp = [[False for _ in range(size)] for _ in range(size)]

        max_len = 1
        start = 0

        for i in range(size):
            dp[i][i] = True

        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    # 表达式 [i + 1, j - 1] 不构成区间，即长度严格小于 2，即 j - 1 - (i + 1) + 1 < 2 ，整理得 j - i < 3。
                    # 不构成区间就是指i到j之间的元素不超过两个，那么头尾相同，那么整个字符串就是回文串
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        # 状态转移，即头尾相同的情况下，里面的子串决定了整个子串是否为回文
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                # 遇到回文(即索引i到j是True)，那么记录开始索引和i到j的长度
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]



if __name__ == '__main__':
    solution = Solution()
    # print(solution.isPalindrome('aba'))
    print(solution.longestPalindrome_4('abbac'))
