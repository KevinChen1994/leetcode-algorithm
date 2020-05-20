# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/20 20:24
'''
solution: 滑动窗口，不难。第一种方法超时了。第二种方法很快。所以思想简单，但是代码细节还是很重要。
'''
from collections import defaultdict
class Solution:
    def findAnagrams_1(self, s: str, p: str):
        ans = []
        n = len(p)
        needs = defaultdict(int)
        for i in p:
            needs[i] += 1
        for i in range(len(s) - n + 1):
            tmp = s[i:n + i]
            tmp_dict = defaultdict(int)
            for j in tmp:
                tmp_dict[j] += 1
            if needs == tmp_dict:
                ans.append(i)
        return ans

    def findAnagrams_2(self, s, p):
        res = []
        window = {}
        needs = {}
        for i in p:
            needs[i] = needs.get(i, 0) + 1
        left, right = 0, 0
        length, limit = len(p), len(s)
        while right < limit:
            c = s[right]
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1
                if (right - left + 1) == length:
                    if window == needs:
                        res.append(left)
                    window[s[left]] -= 1
                    left = left + 1
                right += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    s = "abab"
    p = "ab"
    print(solution.findAnagrams_1(s, p))
