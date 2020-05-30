# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/15 15:01
'''
solution: 先按照身高降序，前边人数升序进行排序。之后让高个子先站好位，思路是当前未排序的序列中最高的按照他前边有几个人作为新序列的索引，因为高个子站好队后，在插入矮个子时，
不会对高个子前边比他高的人数发生变化。所以依次从高个子拍到矮个子就完成了。
'''


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people:
            # list.insert(index, obj)，按照index索引进行插入
            ans.insert(p[1], p)
        return ans


if __name__ == '__main__':
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    print(solution.reconstructQueue(people))
