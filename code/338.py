# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/11 15:13
'''
solution1: 通过观察二进制数，可以发现：
奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。例如：0 = 0;1 = 1;2 = 10;3 = 11
偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
例如：2 = 10;4 = 100;8 = 1000    3 = 11;6 = 110;12 = 1100
solution2: popcount用来计算每一个数含有1的个数，计算方法没看太明白
'''

class Solution:
    def countBits_1(self, num: int):
        result = [0]
        for i in range(1, num+1):
            if i%2 != 0:
                result.append(result[i-1]+1)
            else:
                result.append(result[i//2])
        return result

    def countBits_2(self, num):

        def popcount(n):
            count = 0
            for i in range(n):
                if n == 0: break
                # -的优先级比&高
                n &= n - 1
                count += 1
            return count
        result = []
        for i in range(num + 1):
            result.append(popcount(i))
        return result

if __name__ == '__main__':
    solution = Solution()
    num = 5
    print(solution.countBits_2(num))
