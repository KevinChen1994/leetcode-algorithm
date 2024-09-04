import random
from collections import defaultdict

class RandomizedSet:

    def __init__(self):
        self.nums = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums[val] = 0
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nums:
            return False
        self.nums.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(list(self.nums.keys()))

if __name__ == '__main__':
    randomizedSet = RandomizedSet()
    randomizedSet.insert(1)
    randomizedSet.remove(2)
    randomizedSet.insert(2)
    print(randomizedSet.getRandom())
