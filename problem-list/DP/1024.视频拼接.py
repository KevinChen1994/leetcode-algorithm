from typing import List
'''
题目不难，转移矩阵挺好想的，就是通过小区间推断大区间，但是我一开始使用的二维矩阵，把问题想复杂了。
'''

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [[float('inf')] * (time + 1) for _ in range(time + 1)]

        for clip in clips:
            for i in range(clip[0], clip[1] + 1):
                for j in range(clip[0], clip[1] + 1):
                    if i < j and j <= time:
                        dp[i][j] = 1

        for i in range(time):
            for j in range(i + 1, time + 1):
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        return dp[0][time] if dp[0][time] != float('inf') else -1
    
    def videoStitching2(self, clips: List[List[int]], time: int) -> int:
        dp = [0] + [float('inf')] * time
        for i in range(1, time + 1):
            for left, right in clips:
                if left < i <= right:
                    dp[i] = min(dp[i], dp[left] + 1)
        return dp[time] if dp[time] != float('inf') else -1


if __name__ == '__main__':
    solution = Solution()
    # clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    # time = 10
    clips = [[0, 2], [4, 8]]
    time = 5
    # clips = [[0,5],[6,8]]
    # time = 7
    res = solution.videoStitching(clips, time)
    print(res)
