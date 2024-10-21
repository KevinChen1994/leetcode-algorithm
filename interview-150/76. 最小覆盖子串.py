from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_counter = Counter(t)
        window_counter = Counter()
        requierd = len(t_counter)
        left = 0
        min_len = float('inf')
        min_start = 0
        formed = 0
        for right in range(len(s)):
            # 开始遍历，逐渐移动右指针，目的是寻找满足条件的窗口
            if s[right] in t_counter:
                char = s[right]
                window_counter[char] += 1
                if char in t_counter and window_counter[char] == t_counter[char]:
                    formed += 1
                # 满足条件后，滑动窗口开始遍历，逐渐移动左指针，目的是缩小窗口大小
                while left <= right and formed == requierd:
                    char = s[left]
                    if right - left + 1 < min_len:
                        min_len = right - left + 1
                        min_start = left

                    window_counter[char] -= 1
                    if char in t_counter and window_counter[char] < t_counter[char]:
                        formed -= 1
                    left += 1
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]


                

if __name__ == '__main__':
    solution = Solution()
    print(solution.minWindow(s="ADOBECODEBANC", t="ABC"))  # "BANC"