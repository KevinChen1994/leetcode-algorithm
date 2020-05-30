# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/22 22:19
# software: PyCharm
'''
solution1: 动态规划。问题是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：
G(n): 长度为n的序列的不同二叉搜索树个数。
F(i, n): 以i为根的不同二叉搜索树个数(1 ≤ i ≤ n)。
如果n=3，那么G(3) = F(1,3) + F(2,3) + F(3,3)，即G(n) = ∑F(i,n)。另外，G(0) = 1, G(1) = 1
所以G(n) 可以从 F(i, n) 得到，而 F(i, n) 又会递归的依赖于 G(n)。
例如，F(3,7)，就是二叉搜索树长度为7，以3为根，这时[1,2]为3的左子树，[4,5,6,7]为3的右子树，使用动态规划的思想，
这又是两棵二叉搜索树，所以F(3,7) = G(2)*G(4)，整理成公式为：F(i,n)=G(i−1)⋅G(n−i)
结合上述所说，最终的公式为G(n) = ∑G(i−1)⋅G(n−i)
'''


class Solution:
    def numTrees(self, n):
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        # 控制搜索二叉树的长度
        for i in range(2, n + 1):
            # 控制根的选择
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]


if __name__ == '__main__':
    solution = Solution()
    n = 3
    print(solution.numTrees(n))
