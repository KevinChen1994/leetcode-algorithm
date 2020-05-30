# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/13 17:07
# software: PyCharm
'''
solution 使用动态规划。由后往前去看，如果两个字符串的最后一位相同，那么直接对比word1的前i-1与word2的前j-1位；如果最后一位不同的话，
这里有三种方法进行操作，计算分别使用这三种方法后，哪种方法所需的步数最少。
状态矩阵可以这么想，dp[i][j]的意思就是，将word1的i个字符转换成word2的j个字符，那么下边的这三种操作就不难理解：
dp[i][j - 1] 插入操作，将word1的前i个字符变为word2的前j-1个字符，即在word1后插入一个与word2最后第j个字符相同的字符；
dp[i - 1][j] 删除操作，将word1的前i-1个字符变为word2的前j个字符；
dp[i - 1][j - 1] 替换操作，将word1的前i-1个字符变为word2的前j-1个字符，即将word1最后一个字符替换成word2的最后一个字符
'''


class Solution:
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # 如果word1为空，那么由word1变为word2所需要的步数
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 如果word2为空，那么由word1变为word2所需要的步数
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 这里的加一是加上一次插入、删除或者替换的操作
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    word1 = "horse"
    word2 = "ros"
    print(solution.minDistance(word1, word2))
