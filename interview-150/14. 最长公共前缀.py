from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def isCommonPrefix(index):
            str, count = strs[0][:index], len(strs)
            return all(strs[i][:index] == str for i in range(1, count))

        result = ""
        min_len = float('inf')
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
        
        low, high = 0, min_len
        while low <= high:
            mid = (low + high) // 2
            if isCommonPrefix(mid):
                low = mid + 1
                result = strs[0][:mid]
            else:
                high = mid - 1
        return result
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))

        