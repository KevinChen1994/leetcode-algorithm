

class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
             'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000
        }
        result = 0
        for i in range(len(s) - 1):
            if num_dict[s[i]] >= num_dict[s[i + 1]]:
                result += num_dict[s[i]]
            else:
                result -= num_dict[s[i]]
        result += num_dict[s[-1]]
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.romanToInt('MCMXCIV'))