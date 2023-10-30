

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        # 这里记录了由哪些字母可以生成当前字母
        letters = {'a':['e','i','u'], 'e':['a', 'i'], 'i':['e', 'o'], 'o':['i'], 'u':['i', 'o']}
        # 这里的Map用来标记字母的索引，方便使用
        map = {'a':0, 'e':1,'i':2,'o':3,'u':4}
        # dp[i][j] 中i为字符串长度，j为当前字母，dp[i][j]也就是长度为i时，结尾是j的字符串个数
        dp = [[0] * 5 for _ in range(n)]
        for j in range(5):
            dp[0][j] = 1
        for i in range(1, n):
            for letter, values in letters.items():
                j = map[letter]
                for value in values:
                    temp = map[value]
                    dp[i][j] += dp[i - 1][temp]

        return sum(dp[-1]) % MOD


if __name__ == '__main__':
    solution = Solution()
    res = solution.countVowelPermutation(5)
    print(res)
    