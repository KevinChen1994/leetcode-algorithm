# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/30 22:09
'''
solution1: 暴力法，超时。
solution2: 对solution1的优化，从后往前遍历数组，如果当前数T[i]比他后边的数T[j]小的话，那么结果就是j-i。
如果当前数T[i]比他后边的数T[j]大或者等于，那么如果ans[j]是0的话，说明j后边已经没有比他更大的数了，并且T[i]比T[j]还要大或者等于，所以肯定也没有比T[i]还大的数了。
如果上述两种情况都没有满足，那么可以进行j的跳跃，就是让j加上ans[j]的值，之所以可以这样，是因为T[i]比T[j]还要大或者等于，那就可以直接跟比T[j]大的数进行比较。
solution3: 栈。从左到右遍历数组，栈中存储的是索引。如果当前元素比栈顶元素大，那么结果就是当前值的索引减去栈顶元素的索引，然后出栈；
如果当前元素比栈顶元素小，那就让当前元素索引入栈，继续进行遍历。
'''
class Solution:
    def dailyTemperatures_1(self, T):
        n = len(T)
        ans = [0] * n
        for i in range(n):
            count = 0
            for j in range(i + 1, n):
                if T[j] > T[i]:
                    count += 1
                    ans[i] = j - i
                    break
        return ans

    def dailyTemperatures_2(self, T):
        n = len(T)
        ans = [0] * n
        for i in range(n-2, -1, -1):
            j = i + 1
            while j < n:
                if T[j] > T[i]:
                    ans[i] = j - i
                    break
                # 遇到0表示后面不会有更大的值，那当然当前值就应该也为0
                elif ans[j] == 0:
                    ans[i] = 0
                    break
                # j+= result[j]是利用已经有的结果进行跳跃
                j += ans[j]
        return ans

    def dailyTemperatures_3(self, T):
        n = len(T)
        ans = [0] * n
        stack = []
        for key, value in enumerate(T):
            while len(stack) != 0 and value > T[stack[-1]]:
                ans[stack[-1]] = key - stack[-1]
                stack.pop()
            stack.append(key)
        return ans





if __name__ == '__main__':
    solution = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(solution.dailyTemperatures_3(T))
