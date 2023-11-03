from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[i]定义为长度为3的数组，因为除以3的余数只有3种：0,1,2，dp[i]为余数为i时最大的数组和
        dp = [0, float('-inf'), float('-inf')]
        for num in nums:
            temp = dp[:]
            for i in range(3):
                # 遍历3个余数，计算余数加上当前的数之后的余数，取值为当前余数上一个最大的值或者余数i的最大值加上当前值，取最大
                # 这里将dp矩阵进行复制后进行操作的原因是，在每一个num进行遍历的过程中，转移矩阵都会+num，如果使用同一个dp的话，有可能同一个num添加多次
                # 所以只有使用上一个同样的余数的最大值时使用当前的矩阵temp，如果要使用第i个余数的值时需要使用尚未+num的原始dp矩阵
                temp[(i + num) % 3] = max(temp[(i + num) % 3], dp[i] + num)
            dp = temp    
        return dp[0]


if __name__ == '__main__':
    solution = Solution()
    res = solution.maxSumDivThree([3,6,5,1,8])
    print(res)