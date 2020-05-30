# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/5/28 18:09
'''
solution: 公式推理。先计算出那个任务出现的次数最多，然后将其他的任务插入到两个任务之间。那么公式就是(max_task-1)*(n+1)，
意思就是出现次数最多的元素次数减去1乘上间隔冷却时间加1，为什么加1，因为这样就把出现次数最多的这个元素加进去了，但是最后一个元素没加进去，后边会处理。
这时候就分两种情况。
1：还有一些元素的个数与出现次数最多的元素个数相同，那么势必会在插入之后还剩下一些，这样就可以根据有几个个数跟最多的个数相同来进行相加。参考注释1
2：元素种类过多，导致缝隙不够用，按照之前的公式计算出来，可能比当前tasks数组长度还短，那么就选数组长度作为答案。参考第二条测试数据。
'''


class Solution:
    def leastInterval(self, tasks, n):
        length = len(tasks)
        task_dict = dict()
        for task in tasks:
            task_dict[task] = task_dict.get(task, 0) + 1
        task_sorted = sorted(task_dict.items(), key=lambda x: x[1], reverse=True)
        max_task = task_sorted[0][1]
        ans = (max_task - 1) * (n + 1)
        # 注释1
        for task in task_sorted:
            if task[1] == max_task:
                ans += 1

        return ans if ans >= length else length


if __name__ == '__main__':
    solution = Solution()
    tasks = ["A", "A", "A", "A", "B", "B", "B"]
    tasks = ["A", "A", "A", "B", "C", "D", 'E', 'F', 'G', 'H', 'I']
    n = 2
    print(solution.leastInterval(tasks, n))
