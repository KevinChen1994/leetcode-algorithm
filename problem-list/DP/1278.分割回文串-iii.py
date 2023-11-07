'''
直观上很简单，通过计算上一个状态来推断当前状态，推断过程中，需要通过cost函数计算修改的次数
'''

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if n == k:
            return 0
        # dp[i][j] 为到第i个字母，j个分割，能达成条件的最少字符
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(j, n + 1):
                if j == 1:
                    dp[i][j] = self.cost(s[:i])
                else:
                    # 如果j > 1，需要将字符串进行切割，切割成几个字符串取决于j的大小
                    # 遍历从j - 1开始，依次进行推断，并保留最小值
                    # x为切割的位置，切割后修改成回文字符串的修改次数为从0到x的子串，切割次数减一次的最小次数，加上字符串从x到i的子串需要修改的次数
                    for x in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[x][j - 1] + self.cost(s[x:i]))
        return dp[-1][-1]
    
    # 计算当前字符串变成回文字符串需要修改的次数
    def cost(self, s):
        res = 0
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                res += 1
            left += 1
            right -= 1    
        return res




if __name__ == '__main__':
    solution = Solution()
    res = solution.palindromePartition('abc', 2)
    print(res)