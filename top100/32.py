# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/2/28 10:54
# software: PyCharm

'''
最长有效括号，得是连续的，比如(()(()，这个最长是2，因为有两个有效的()，但是没有连续。
方法1：使用栈，先把-1放到栈中，是为了防止第一个是）导致栈内没有元素就直接pop会报错。
判断如果是(，就将该元素的索引放到栈中，遇到)就将栈顶元素退栈，并计算当前元素的索引与弹出的索引的差即为有效括号的长度
另外，如果栈为空，将当前元素放到栈中。
'''


class Solution:
    # 使用栈
    def longestValidParentheses_1(self, s):
        stack = [-1]
        maxans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])

        return maxans

    # 动态规划
    def longestValidParentheses_2(self, s):
        s_len = len(s)
        dp = [0 for _ in range(s_len + 1)]
        for i in range(1, s_len):
            if s[i] == ")":
                # 当前的位置需要减去前一个有效括号长度，还有减1，才能到达未匹配的括号的位置
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    # 当前位置的有效括号长度为前一个有效括号加2
                    dp[i] = dp[i - 1] + 2
                    # 当前位置减去前边的有效括号长度，再减去2，定位到连续有效括号之前的位置，如果大于0，说明这个位置可能还有连续括号
                    if i - dp[i - 1] - 2 >= 0:
                        # 将当前值的有效括号个数加上与之相连的有效括号个数
                        dp[i] += dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses_2(')()(())'))
