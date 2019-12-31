# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2019/12/30 21:31
# software: PyCharm


'''
这道题借助滑动窗口来做比较简单。
1 最开始我使用的temp是一个list，将连续不重复的字符串放到list中，在遍历过程中如果遇到与temp里相同的字符，
则从list中pop掉第一个，同时记录temp的最大长度就是无重复最长子串
2 看到评论区有人也用滑动窗口的方法，但是速度比我的快30ms，我对比了一下，时间花费在list上，于是将list替换成set，
速度马上就上去了，但是set不能用pop，因为set是无序的，pop删掉的可能不是第一个字符，于是用left记录当前set中第一个字符的索引。
总结：set确实快，查了资料发现，如果list和set长度超过1000，set的速度基本不会变化，但list会降低好多好多。
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        max = 0
        left = 0
        cur_len = 0
        temp = set()
        for i in range(len(s)):
            cur_len += 1
            while s[i] in temp:
                temp.remove(s[left])
                left += 1
                cur_len -= 1
            temp.add(s[i])
            if cur_len > max: max = cur_len
        return max


if __name__ == '__main__':
    solution = Solution()
    s = 'dvdf'
    print(solution.lengthOfLongestSubstring(s))
