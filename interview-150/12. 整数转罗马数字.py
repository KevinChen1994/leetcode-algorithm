

class Solution:
    def intToRoman(self, num: int) -> str:
        if num < 1 or num > 3999:
            return ""
        result = ""
        if num >= 1000:
            result += "M" * (num // 1000)
            num = num % 1000
        if num >= 900:
            result += "CM"
            num = num - 900
        if num >= 500:
            result += "D"
            num = num - 500
            if num < 400:
                result += "C" * (num // 100)
                num = num % 100
        if num >= 400:
            result += "CD"
            num = num - 400
        if num >= 100:
            result += "C" * (num // 100)
            num = num % 100
        if num >= 90:
            result += "XC"
            num  = num - 90
        if num >= 50:
            result += "L"
            num = num - 50
            if num < 40:
                result += "X" * (num // 10)
                num = num % 10
        if num >= 40:
            result += "XL"
            num = num - 40
        if num >= 10:
            result += "X" * (num // 10)
            num = num % 10
        if num >= 9:
            result += "IX"
            num = num - 9
        if num >= 5:
            result += "V"
            num = num - 5
            if num < 4:
                result += "I" * num
                num = 0
        if num >= 4:
            result += "IV"
            num = num - 4
        if num >= 1:
            result += "I" * num
        return result
    
    # 贪心
    def intTORoman2(self, num: int) -> str:
        num_dict = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in num_dict:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += num_dict[key] * count 
                num %= key
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.intTORoman2(num=11))