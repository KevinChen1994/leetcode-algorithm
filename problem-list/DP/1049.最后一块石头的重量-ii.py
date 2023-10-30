from typing import List


'''
这道题与416是一样的问题，416需要做的是将数组拆分成两个数组，使其目标和一致。这道题也是需要进行拆分，使其最终的“和”最小，这里“和”的计算是能够消除最小的数的。
那就可以转换成01背包问题，首先确定目标是什么，416能够很简单的看出来就是数组和的一半，这道题也可以设置为数组和的一半，因为这样才能保证最终的“和”结果最小。
最终获取结果的时候，只需要从后往前遍历dp数组就行，遇到的第一个能凑出来的数，使用总和减去这个数的二倍就是最终的剩下的“和”。
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = dp[j] or dp[j - stone]
        ans = None
        for j in range(target, -1, -1):
            if dp[j]:
                ans = total - 2 * j
                break
        return ans


if __name__ == '__main__':
    solution = Solution()
    res = solution.lastStoneWeightII([2,7,4,1,8,1])
    print(res)