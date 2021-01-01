# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/7/18 21:55

class Solution:
    def countBits(self, num: int):
        result = [0]
        for i in range(1, num + 1):
            if i % 2 != 0:
                result.append(result[i - 1] + 1)
            else:
                result.append(result[i // 2])
        return result

