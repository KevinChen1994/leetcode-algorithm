


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        ransomNote_dict = {}
        for i in magazine:
            magazine_dict[i] = magazine_dict.get(i,0) + 1
        for i in ransomNote:
            ransomNote_dict[i] = ransomNote_dict.get(i,0) + 1
        for k,v in ransomNote_dict.items():
            if k not in magazine_dict or magazine_dict[k] < v:
                return False
        return True

if __name__ == '__main__':
    solution =Solution()
    print(solution.canConstruct('aa','aab')) # True