# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2019/12/27 14:45
# software: PyCharm

def twoSum(nums, target):
    num_dict = {}
    for index, num in enumerate(nums):
        if target - num in num_dict:
            return num_dict[target - num], index
        else:
            num_dict[num] = index
    return []


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
