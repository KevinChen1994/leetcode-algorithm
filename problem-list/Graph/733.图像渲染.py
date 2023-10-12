# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2021/1/27 18:14
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        if m == 0:
            return image
        n = len(image[0])
        originColor = image[sr][sc]
        self.dfs(image, sr, sc, m, n, newColor, originColor)

        return image

    def dfs(self, image, sr, sc, m, n, newColor, originColor):
        if sr < 0 or sc < 0 or sr >= m or sc >= n or image[sr][sc] != originColor or image[sr][sc] == newColor:
            return
        image[sr][sc] = newColor
        self.dfs(image, sr - 1, sc, m, n, newColor, originColor)
        self.dfs(image, sr + 1, sc, m, n, newColor, originColor)
        self.dfs(image, sr, sc - 1, m, n, newColor, originColor)
        self.dfs(image, sr, sc + 1, m, n, newColor, originColor)


if __name__ == '__main__':
    solution = Solution()
    # image = [
    #     [1, 1, 1],
    #     [1, 1, 0],
    #     [1, 0, 1]
    # ]
    image = [[0, 0, 0], [0, 0, 0]]
    sr = 0
    sc = 0
    newColor = 2
    print(solution.floodFill(image, sr, sc, newColor))
