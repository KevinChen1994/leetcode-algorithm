# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2020/1/16 13:38
# software: PyCharm

class Solution:
    def letterCombinations(self, digits):
        dict = {'2': ['a', 'b', 'c'],
                '3': ['d', 'e', 'f'],
                '4': ['g', 'h', 'i'],
                '5': ['j', 'k', 'l'],
                '6': ['m', 'n', 'o'],
                '7': ['p', 'q', 'r', 's'],
                '8': ['t', 'u', 'v'],
                '9': ['w', 'x', 'y', 'z']}
        result = []
        if len(digits) == 0:
            return result
        if len(digits) > 1:
            new_digits = digits[1:]
            former = self.letterCombinations(new_digits)
            for i in former:
                for j in dict[digits[0]]:
                    result.append((j + i))
        else:
            result = dict[digits]

        return result



if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations('23'))
