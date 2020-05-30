# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/3/10 17:32
# software: PyCharm
'''
思路：先将整个list按照第一个元素排序，之后遍历记录merged数组，如果merged的第二个元素小于
下一个数组的第一个元素，那么将两个数组合并，否则重新记录下一个数组。
'''
class Solution:
    def merge(self, intervals):
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == '__main__':
    solution = Solution()
    intervals = [[1, 3], [2, 6], [9, 13], [8, 10], [15, 18]]
    print(solution.merge(intervals))
