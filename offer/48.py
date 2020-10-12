# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/29 14:45

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_len = 0
        tmp = set()
        left = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] not in tmp:
                tmp.add(s[i])
                cur_len += 1
            else:
                while s[i] in tmp:
                    tmp.remove(s[left])
                    left += 1
                    cur_len -= 1
                tmp.add(s[i])
                cur_len += 1
            max_len = max(max_len, cur_len)
        return max_len


if __name__ == '__main__':
    solution = Solution()
    s = 'abcabcb'
    print(solution.lengthOfLongestSubstring(s))
