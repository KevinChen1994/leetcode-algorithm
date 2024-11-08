

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for i, j in zip(s, t):
            s_dict[i] = s_dict.get(i, 0) + 1
            t_dict[j] = t_dict.get(j, 0) + 1
        return s_dict == t_dict

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram("a", "ab"))  # True