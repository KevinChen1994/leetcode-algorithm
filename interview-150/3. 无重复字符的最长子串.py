

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = right = 0
        res = 1
        while left < len(s) and right <= len(s):
            if len(s[left:right]) == len(''.join(set(s[left:right]))):
                res = max(res, len(s[left:right]))
                right += 1
            else:
                left += 1
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("au"))