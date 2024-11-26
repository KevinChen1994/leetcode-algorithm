
class Solution:
    def isHappy(self, n: int) -> bool:
        while n != 1 and n != 4:
            n = sum([int(i) ** 2 for i in str(n)])
        return n == 1
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(n=116))  # True