

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split()
        if len(pattern) != len(s_split):
            return False
        p_dict = {}
        for p, c in zip(pattern, s_split):
            if p in p_dict:
                if p_dict[p] != c:
                    return False
            else:
                p_dict[p] = c
        return len(set(p_dict.values())) == len(p_dict.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.wordPattern('abba','dog cat cat dog')) # True