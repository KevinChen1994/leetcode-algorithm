# 二进制

## 常见二进制操作

### 位运算概览

| 符号 | 描述 | 运算规则                                                     |
| :--- | :--- | :----------------------------------------------------------- |
| &    | 与   | 两个位都为1时，结果才为1                                     |
| \|   | 或   | 两个位都为0时，结果才为0                                     |
| ^    | 异或 | 两个位相同为0，相异为1                                       |
| ~    | 取反 | 0变1，1变0                                                   |
| <<   | 左移 | 各二进位全部左移若干位，高位丢弃，低位补0                    |
| >>   | 右移 | 各二进位全部右移若干位，对无符号数，高位补0，有符号数，各编译器处理方法不一样，有的补符号位（算术右移），有的补0（逻辑右移） |

### 基本操作

a=0^a=a^0

0=a^a

由上面两个推导出：a=a^b^b

### 交换两个数

a = a^b

b = a^b

a = a^b

### 移除最后一个1

a = n&(n-1)

### 获取最后一个1

diff=(n&(n-1))^n

## 练习

### single-number

[single-number](https://leetcode-cn.com/problems/single-number/)

> 给定一个**非空**整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

```python
'''
solution: 使用异或运算，两个数相同为0，不同为1；因为异或操作满足交换律，例如:1^2^2=2^2^1=0^1=1（0异或任意数是等于任意数本身）
'''
class Solution:
    def singleNumber(self, nums):
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 2, 2]
    print(solution.singleNumber(nums))
```

### single-number-iii

[single-number-iii](https://leetcode-cn.com/problems/single-number-iii/)

> 给定一个整数数组 `nums`，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

```python
'''
solution: 想办法将nums分成两组，每组分别包含1个只出现一次的数字，两组分别异或就得到两个只出现一次的数字。
首先将全部数组进行异或，最终的结果就是两个只出现一次的数字的异或结果。如果某一位是1，就意味着另一个数组的这个位置是0。
'''
class Solution:
    def singleNumber(self, nums):
        bitmask = 0
        for num in nums:
            bitmask = bitmask ^ num
        # 保留bitmask最右边的1，这个1要么来自x，要么来自y
        diff = bitmask & (-bitmask)
        x = 0
        for num in nums:
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 1, 3, 2, 5]
    print(solution.singleNumber(nums))
```

### num-of-1-bits

[number-of-1-bits](https://leetcode-cn.com/problems/number-of-1-bits/)

> 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为[汉明重量](https://baike.baidu.com/item/汉明重量)）。

```python
'''
solution: 将n与1进行与运算，得到n的最低位数字，再将n右移。
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count
```

### counting-bits

[counting-bits](https://leetcode-cn.com/problems/counting-bits/)

> 给定一个非负整数 **num**。对于 **0 ≤ i ≤ num** 范围中的每个数字 **i** ，计算其二进制数中的 1 的数目并将它们作为数组返回。

```python
class Solution:
    def countBits(self, num: int):
        result = [0]
        for i in range(1, num + 1):
            if i % 2 != 0:
                result.append(result[i - 1] + 1)
            else:
                result.append(result[i // 2])
        return result
```

### reverse-bits

[reverse-bits](https://leetcode-cn.com/problems/reverse-bits/)

> 颠倒给定的 32 位无符号整数的二进制位

```python
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

```

