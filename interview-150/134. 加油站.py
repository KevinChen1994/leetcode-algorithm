from typing import List

'''
实际计算过程中，不管油箱空没空都可以继续计算的。
想通这一点，就可以通过一次循环跑完所有加油站，计算总剩余油量和当下剩余油量了。
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas, remain_gas, start = 0, 0, 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            remain_gas += gas[i] - cost[i]

            if remain_gas < 0:
                start = i + 1
                remain_gas = 0
        return start if total_gas >= 0 else -1
            

if __name__ == '__main__':
    solution = Solution()
    # gas = [1,2,3,4,5]
    # cost = [3,4,5,1,2]
    gas = [2,3,4]
    cost = [3,4,3]
    print(solution.canCompleteCircuit(gas, cost))