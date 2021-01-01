# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/4 10:42
'''
solution: 01背包问题，定义背包容量大小的dp数组，记录每一个容量能取得的最大价值。
动态转移方程为：如果将当前元素添加到背包中，那么新的总价值为dp[当前容量-当前元素大小] + 当前元素价值；如果不添加当前元素，那么价值为dp[当前容量]
选择最大的即可。
另外，可以将该方法进行封装，在一系列背包问题中都可以使用。
'''


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        dp = [0 for _ in range(m + 1)]
        # 遍历每一个元素的大小
        for i in range(n):
            # 从背包容量开始遍历到当前元素的大小
            for v in range(m, A[i] - 1, - 1):
                # 将当前元素加到背包中，与不添加该元素，哪一个价值更高选哪个
                dp[v] = max(dp[v], dp[v - A[i]] + V[i])

        return dp[m]

    def backPackII_2(self, m, A, V):
        n = len(A)
        if n == 0:
            return 0
        dp = [0 for i in range(m + 1)]

        # 将该思路封装，在其他背包问题中可以进行使用
        def zero_one_backpack(dp, m, A, V):
            for v in range(m, A - 1, -1):
                dp[v] = max(dp[v], dp[v - A] + V)

        for i in range(n):
            zero_one_backpack(dp, m, A[i], V[i])
        return dp[m]


if __name__ == '__main__':
    solution = Solution()
    m = 10
    A = [2, 3, 5, 7]
    V = [1, 5, 2, 4]
    # m = 100
    # A = [77, 22, 29, 50, 99]
    # V = [92, 22, 87, 46, 90]
    print(solution.backPackII_2(m, A, V))
