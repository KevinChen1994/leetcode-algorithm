# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/15 15:23
# software: PyCharm
'''
solution：滑动窗口，使用前后两个指针来作为滑动窗口，首先右指针先移动，一直到滑动窗口内的字符串包含全部子串的字符，此时移动左指针，
每移动一次，记录一下滑动窗口最小的长度，直到滑动窗口内的字符串不包含子串的全部字符。循环的终止就是右指针指向字符串的最后一个字符。
如果判断滑动窗口内的字符包含子串的全部字符：通过Counter的字典来实现。详见代码。

float('inf') 表示正无穷；float('-inf') 表示负无穷
all(iterable) 用来判断可迭代参数iterable是否都为True，如果是返回True，否则返回False
map() 会根据提供的函数对指定序列做映射。
>>> map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
'''


class Solution:
    def minWindow_1(self, s, t):
        from collections import Counter
        left = 0
        right = 0
        t = Counter(t)
        lookup = Counter()
        min_len = float('inf')
        res = ''
        while right < len(s):
            lookup[s[right]] += 1
            right += 1
            # 这里写的贼秒！
            # 从里往外看，先看t.keys()，这里是子串的一个列表，通过匿名函数，判断，lookup字典中每一个key是否都大于等于t中的每个元素的个数；
            # 那么就会生成一个True和False的列表，再通过all()方法，判断如果都是True那么说明当前滑动窗口下的字符串满足要求，否则不满足。
            while all(map(lambda x: lookup[x] >= t[x], t.keys())):
                if right - left < min_len:
                    res = s[left: right]
                    min_len = right - left
                lookup[s[left]] -= 1
                left += 1
        return res

    def minWindow_2(self, s, t):
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    s = 'ADOBECODEBANC'
    t = 'ABC'
    # s = 'bbaa'
    # t = 'aba'
    print(solution.minWindow_2(s, t))
