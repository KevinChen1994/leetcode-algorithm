# -*- coding:utf-8 -*-
# author:chenmeng
# datetime:2019/12/27 14:45
# software: PyCharm

# 在循环中，将数组中的值依次放到字典中，判断target与当前值的差是否在字典中，如在在，说明当前值与字典中的这个值相加等于target
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
