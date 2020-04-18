# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/4/16 18:15
'''
本题可以转换为是否存在有向无环图，因为课程有前提，不能存在任何环路，如果存在则不成立。可以通过拓扑排序判断是否存在有向无环图。
solution1: 入度表（广度优先遍历）
solution2: 深度优先遍历
'''
from collections import deque


class Solution:
    # BFS
    def canFinish_1(self, numCourses: int, prerequisites) -> bool:
        # 入度
        indegrees = [0 for _ in range(numCourses)]
        # 邻接表
        adjacency = [[] for _ in range(numCourses)]
        queue = deque()
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        for i in range(len(indegrees)):
            # 如果没有一个点没有入度，就进入到队列中（没有入度说明可以没有前提课程，可以直接上）
            if not indegrees[i]:
                queue.append(i)
        while queue:
            pre = queue.popleft()
            numCourses -= 1
            # 遍历以当前这个点为前提的课程
            for cur in adjacency[pre]:
                # 上边已经上完那节课了，所以当前这个点的入度需要减一
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        # 如果全部课都上完，return True
        return not numCourses

    # DFS
    def canFinish_2(self, numCourses, prerequisites):

        def dfs(i, adjacency, flags):
            # 如果是-1，说明已经被其他节点启动的DFS访问过了，直接返回True
            if flags[i] == -1: return True
            # 如果是1，说明在本轮DFS中第二次被访问，说明有环存在，返回False
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        # 0 未被访问； -1 已被其他节点访问； 1 被当前节点访问
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags): return False
        return True


if __name__ == '__main__':
    solution = Solution()
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    # prerequisites = [[1, 0], [2, 1], [3, 1], [4, 2]]
    print(solution.canFinish_2(numCourses, prerequisites))
