from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in str_dict:
                str_dict[key].append(str)
            else:
                str_dict[key] = [str]
        return list(str_dict.values())

if __name__ == '__main__':
    solution = Solution()
    print(solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["ate","eat","tea"],["nat","tan"],["bat"]]