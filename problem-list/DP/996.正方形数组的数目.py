from typing import List
import collections
import math

class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        count = collections.Counter(nums)

        graph = {x:[] for x in count}

        for x in count:
            for y in count:
                if int((x + y) ** 0.5 + 0.5) ** 2 == x + y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(nums) - 1) for x in count)
    
    def numSquarefulPerms2(self, nums: List[int]):
        def edge(x, y):
            r = math.sqrt(x + y)
            return int (r + 0.5) ** 2 == x + y
        
        graph = [[] for _ in range(len(nums))]

        for i, x in enumerate(nums):
            for j in range(i):
                if edge(x, nums[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        @lru_cache(None)
        def dfs(node, visited):
            if visited == (i << len(nums)) - 1:
                return 1
            
            ans = 0
            for nei in graph[node]:
                if (visited >> nei) & 1 == 0:
                    ans += dfs(nei, visited | (1 << nei))
            return ans
        
        ans = sum(dfs(i, 1<<i) for i in range(N))
        count = collections.Counter(A)
        for v in count.values():
            ans //= math.factorial(v)
        return ans





if __name__ == '__main__':
    solution = Solution()
    nums = [1,17,8]
    # [1, 8, 17] [17, 8, 1]
    print(solution.numSquarefulPerms(nums))