# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/21 20:03
'''
solution1: 内置函数bin()返回二进制数，x^y，^是按位异或运算符，当两对应的二进位相异时，结果为1
solution2: 移位，判断是否为1。
solution3: 布赖恩·克尼根算法
'''
class Solution:
    def hammingDistance_1(self, x, y):
        return bin(x ^ y).count('1')

    def hammingDistance_2(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            # & 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
            if xor & 1:
                distance += 1
            xor = xor >> 1
        return distance

    def hammingDistance_3(self, x, y):
        xor = x ^ y
        distance = 0
        while xor:
            distance += 1
            # remove the rightmost bit of '1'
            xor = xor & (xor - 1)
        return distance



if __name__ == '__main__':
    solution = Solution()
    x = 1
    y = 4
    print(solution.hammingDistance_2(x, y))
