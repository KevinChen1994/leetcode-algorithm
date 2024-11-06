

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_dict = {}
        for i, j in zip(s, t):
            if i in char_dict:
                if char_dict[i] != j:
                    return False
            else:
                char_dict[i] = j
        # 保证一个字符只能映射到一个字符
        return len(set(char_dict.values())) == len(char_dict.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.isIsomorphic('abdc','baba')) # True