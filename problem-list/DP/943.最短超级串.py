from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n, mask = len(words), 1 << len(words)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                l1 = len(words[i])
                length = min(len(words[i]), len(words[j]))
                for k in range(length, 0, -1):
                    if words[i][l1 - k:] == words[j][:k]:
                        dp[i][j] = k
                        break

        f = [[0 for _ in range(n)] for _ in range(mask)]
        p = [[0 for _ in range(n)] for _ in range(mask)]
        for s in range(mask):
            for i in range(n):
                if (s >> i) & 1 == 0:
                    continue
                for j in range(n):
                    if (s >> j) & 1 == 1:
                        continue
                    if f[s | (1 << j)][j] <= f[s][i] + dp[i][j]:
                        f[s | (1 << j)][j] = f[s][i] + dp[i][j]
                        p[s | (1 << j)][j] = i
        
        max_val = f[mask - 1][0]
        idx, last, status = 0, -1, mask - 1        
        for i in range(1, n):
            if max_val < f[mask - 1][i]:
                max_val = f[mask - 1][i]
                idx = i
        ans = ""
        while status != 0:
            if last == -1:
                ans = words[idx]
            else:
                ans = words[idx][:len(words[idx]) - dp[idx][last]] + ans
            last = idx
            idx = p[status][idx]
            status ^= 1 << last
        return ans

if __name__ == '__main__':
    solution = Solution()
    words = ["catg","ctaagt","gcta","ttca","atgcatc"]
    # "gctaagttcatgcatc"
    res = solution.shortestSuperstring(words)
    print(res)