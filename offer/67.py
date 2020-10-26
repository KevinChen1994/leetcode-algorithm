# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/10/26 17:11
'''
solution: 因为有最大和最小的限制，所以需要设置一个边界，边界为最大值除以10：2147483647 // 10 = 214748364，
所以如果大于边界值，那么后边无论是哪个数字最终都会大于最大值或者小于最小值；如果等于边界值，这时需要判断当前数字，
如果大于7的话，那么与上边的情况相同，如果小于7，那还可以在加上一位。
'''
class Solution:
    def strToInt(self, str) -> int:
        res = 0
        max_num, min_num, boundray = 2 ** 31 - 1, -1 * 2 ** 31, (2 ** 31 - 1) // 10
        str = str.strip()
        if not str:
            return res
        negative = False
        index = 0
        if str[0] == '-':
            negative = True
            index = 1
        elif str[0] == '+':
            negative = False
            index = 1
        for i in range(index, len(str)):
            if not '0' <= str[i] <= '9':
                break
            elif res > boundray or res == boundray and str[i] > '7':
                return max_num if not negative else min_num
            res = 10 * res + int(str[i])

        return -1 * res if negative else res


solution = Solution()
str = '+1'
print(solution.strToInt(str))
