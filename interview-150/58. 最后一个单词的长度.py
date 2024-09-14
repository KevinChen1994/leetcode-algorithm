

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))