# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/2 22:46
'''
solution: 使用dp记录每个容量是够可以凑齐，然后选出最大的可以凑齐的容量就是结果。
首先将背包中第一个元素在dp数组中设置为True，因为如果这个元素小于背包总容量的话，那么他所代表的容量就能凑齐。
然后从第二个元素开始遍历背包内的元素，内层循环为，背包总容量减去当前遍历的元素，看背包中剩下的元素谁能凑齐这些容量，
如果凑齐，那么dp[j + A[i]] = True. 原因是dp[j]可以凑齐，dp[A[i]]也可以凑齐，那么他俩相加的容量肯定也能凑齐。
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        if A[0] <= m:
            dp[A[0]] = True
        # 遍历背包元素
        for i in range(1, n):
            # 从背包容留减去当前遍历到的元素A[i]开始进行遍历，这个就是当前最大容量。
            # 如果dp数组中已经有可以凑齐当前值dp[j]的元素，那么这两个和肯定也能凑齐。
            for j in range(m - A[i], -1, -1):
                if dp[j] == True:
                    dp[j + A[i]] = True
        # 从最大容量开始遍历，如果为True，说明可以凑齐，然后返回，如果一直没有返回说明不能凑齐。
        for i in range(m, -1, -1):
            if dp[i] == True:
                return i

        return 0


if __name__ == '__main__':
    solution = Solution()
    m = 10
    A = [3, 4, 8, 5]
    print(solution.backPack(m, A))
