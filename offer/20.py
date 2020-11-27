# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/8/25 21:51
'''
solution1: 通过观察总结出有效数字具有以下几个特点：
+-出现在开头或者e后边；
e之前不能有e，必须有数；
小数点之前不能出现小数点或者e。
需要注意：测试用例中首尾可能出现空格，这种不影响他是不是一个有效的数字，如果空格出现在中间那么就不是一个数字。
solution2: 使用编译原理的有限状态自动机，然而我没看太懂，对不起于老师。。。
有效状态自动机讲解：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/mian-shi-ti-20-biao-shi-shu-zhi-de-zi-fu-chuan-y-2/
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        if len(s) == 0:
            return False
        num_seen = False
        dot_seen = False
        e_seen = False
        # 去除首尾的空格。
        s = s.strip()
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                num_seen = True
            elif s[i] == '.':
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif s[i] == 'e' or s[i] == 'E':
                if e_seen or not num_seen:
                    return False
                e_seen = True
                # 重置num_seen，防止123e，或者123e+的情况，确保e之后也出现数字
                num_seen = False
            elif s[i] == '-' or s[i] == '+':
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            else:
                return False
        return num_seen


if __name__ == '__main__':
    solution = Solution()
    s = '1 '
    print(solution.isNumber(s))
