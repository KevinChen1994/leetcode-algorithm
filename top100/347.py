# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/11 16:33
'''
solution1: 先构建一个数字:词频的字典，然后在构建一个词频:数字的字典，从序列长度开始遍历，这就相当于是最大的重复次数，存储到序列中，输出前k个即可。
solution2: 使用现成的库就可以计算出重复次数。
'''

from collections import Counter


class Solution:
    def topKFrequent(self, nums, k):
        ans = []
        dict_ = {}
        for num in nums:
            if num in dict_:
                dict_[num] += 1
            else:
                dict_[num] = 1
        dict__ = {}
        for num, n in dict_.items():
            if n in dict__:
                dict__[n].append(num)
            else:
                dict__[n] = [num]
        for i in range(len(nums), 0, -1):
            if i in dict__:
                for j in dict__[i]:
                    ans.append(j)
        return ans[:k]


    def topKFrequent(self, nums, k):

        return [x[0] for x in Counter(nums).most_common(k)]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(solution.topKFrequent(nums, k))
