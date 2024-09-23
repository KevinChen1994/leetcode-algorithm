

class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = s.strip().split()
        n = len(str_list)
        left, right = 0, n - 1
        while left < right:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1
        return " ".join(str_list)

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("the sky is blue"))