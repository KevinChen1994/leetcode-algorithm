# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/29 22:45
'''
solution1: 动态规划。使用动态转移矩阵来记录每一个位置的最小平方数个数。转移矩阵的计算方法为 dp[i] = min(dp[i], dp[i-j*j]+1)
首先每一个位置的dp初始值都为当前索引的值，具体原因为如果当前这个位置的数没有符合的平方数，保底也有n个1相加，也就是当前位置的索引的值。
然后设置一个j，所谓j就是平方数在平方之前的值，从1开始，一直累加，知道当前值i-j*j < 0为止，这时在判断dp[i-j*j]+1与dp[i]的大小,
i-j*j就是当前值减去一个平方数，之后在动态规划这个过程。。。
solution2: BFS。使用队列记录(当前数减去平方数的差,步数)，使用广度优先搜索，计算当前数减去从1开始的平方数，直至小于0为止，记录所有的差值和步数，
并存储到队列中，然后遍历队列，继续使用广度优先搜索，进行相同的操作。在遍历的过程中，需要对比差值是否为0，如果是0说明已经找到了对应的平方数的和，
并且需要在visited中记录已经访问过的差值，避免重复计算。
'''
class Solution:
    def numSquares_1(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        for i in range(n+1):
            dp[i] = i
            j = 1
            while i - j*j >= 0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

    def numSquares_2(self, n):
        from collections import deque
        deq = deque()
        visited = set()

        deq.append((n, 0))
        while deq:
            number, step = deq.popleft()
            targets = [number - i * i for i in range(1, int(number ** 0.5) + 1)]
            for target in targets:
                if target == 0: return step + 1
                if target not in visited:
                    deq.append((target, step + 1))
                    visited.add(target)
        return 0

if __name__ == '__main__':
    solution = Solution()
    n = 13
    print(solution.numSquares_2(n))