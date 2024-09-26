

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 去除空格和非字母数字字符
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(s = "A man, a plan, a canal: Panama"))