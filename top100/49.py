#-*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/4 22:08
# software: PyCharm
'''
collections.defaultdict(list)创建的是一个value值为list的字典，直接使用dict的话，不能用tuple作为key。
总结一下tuple的几个用法：
>>>tuple([1,2,3,4])
(1, 2, 3, 4)
>>> tuple({1:2,3:4})    #针对字典 会返回字典的key组成的tuple
(1, 3)
>>> tuple((1,2,3,4))    #元组会返回元组自身
(1, 2, 3, 4)


'''

import collections


class Solution:
    def groupAnagrams_1(self, strs):
        ans = collections.defaultdict(list)
        for word in strs:
            # 这里使用tuple将list转成tuple类型，这样才可以作为key。
            ans[tuple(sorted(word))].append(word)
        return list(ans.values())

    def groupAnagrams_2(self,strs):
        ans = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for w in word:
                # ord()返回的是一个字符的ASCII数值
                count[ord(w) - ord('a')] += 1
            ans[tuple(count)].append(word)
        return list(ans.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams_2(strs))