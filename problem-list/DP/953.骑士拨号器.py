
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        # 先计算每个号码能够到达的数字位置
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9],
                 [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        # 定义dp数组，dp[i][j]代表，在i步，数字j下能拨打的电话长度
        dp = [[0] * 10 for _ in range(n)]

        for i in range(n):
            if i == 0:
                # 因为输入一个数字时，所有数字都是可以的，所以设置为1
                dp[0] = [1] * 10
                continue
            for j in range(10):
                for index, move in enumerate(moves):
                    # 判断当前数字是由哪些数字移动过来的，通过dp累加路径和
                    if j in move:
                        dp[i][j] += (dp[i-1][index] % MOD)
        return sum(dp[-1]) % MOD


if __name__ == '__main__':
    solution = Solution()
    res = solution.knightDialer(1)
    print(res)
