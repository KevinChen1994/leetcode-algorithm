

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle: 
                return i
            
if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr("hello", "ll"))