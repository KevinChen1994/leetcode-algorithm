# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/4/2 22:51
# software: PyCharm
'''
solution: 将nums放到set()中，实现 O(1) 时间的查询。如果num-1不在序列中，说明num是序列中，可以num为开头查找连续序列。
接下来就是while遍历，每次给num+1，同时记录最大的长度。
时间复杂度看上去像是O(n²)，但是实际是O(n)。因为这是一个线性的算法，只有遇到一个连续序列的开始，他才会用while去查找连续的序列，
如果不是连续序列的开始，就不会去执行while。while在整个循环过程中只会被迭代n次，所以看上去是O(n*n)，实际是O(n+n)
'''
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            # 如果num-1在num_set中的话，那num肯定不是最长序列的开头
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == '__main__':
    solution = Solution()
    nums = [100, 4, 200, 1, 2, 3]
    print(solution.longestConsecutive(nums))
