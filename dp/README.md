# 动态规划

## 背景

先从一到题目开始

[triangle](https://leetcode-cn.com/problems/triangle/)

> 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
>
> 相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
>
> 例如，给定三角形：
>
> [
>      [2],
>     [3,4],
>    [6,5,7],
>   [4,1,8,3]
> ]
> 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
>

使用DFS（遍历或者分治法）

超时

```Python
# DFS 超时。f(i,j)=min(f(i+1,j),f(i+1,j+1))+triangle[i][j]
class Solution:
    def minimumTotal(self, triangle):
        return self.dfs(0, 0, triangle)

    def dfs(self, level, c, triangle):
        if level == len(triangle):
            return 0
        left = self.dfs(level + 1, c, triangle)
        right = self.dfs(level + 1, c + 1, triangle)
        return min(left, right) + triangle[level][c]
```

优化DFS，添加备忘录功能（称为记忆化搜索，本质上就是动态规划）

```Python
# DFS 带有备忘录，减少运算
class Solution:
    def minimumTotal(self, triangle):
        self.memo = [[0 for i in range(len(triangle))] for j in range(len(triangle))]
        return self.dfs(0, 0, triangle)

    def dfs(self, level, c, triangle):
        if level == len(triangle):
            return 0
        if self.memo[level][c] != 0:
            return self.memo[level][c]
        self.memo[level][c] = min(self.dfs(level + 1, c, triangle), self.dfs(level + 1, c + 1, triangle)) + triangle[level][c]
        return self.memo[level][c]
```

DP

```Python
# DP dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]
```

动态规划就是把大问题变成小问题，并解决了小问题重复计算的方法。

## 动态规划和DFS的区别

- 二叉树子问题是没有交集，所以大部分二叉树都是用递归或者分治法，即DFS，就可以解决问题。
- 像triangle这种是有重复走的情况，**子问题是有交集的**，所以可以用动态规划来解决。

**动态规划的三个特性：**

- 最优子结构

最优子结构指的是，问题的最优解包含子问题的最优解。反过来说就是，我们可以通过子问题的最优解，推导出问题的最优解。如果我们把最优子结构，对应到我们前边定义的动态规划问题的模型上，那我们也可以理解为，后面阶段的状态可以通过前面阶段的状态推导出来。

- 无后效性

无后效性有两层含义，第一层含义是，在推导后面阶段的状态的时候，我们只关心前面阶段的状态值，不关心这个状态是怎么一步一步推导出来的。第二层含义是，某阶段状态一旦确定，就不受之后阶段的决策影响。无后效性是一个非常“宽松”的要求。只要满足前面提到的动态规划问题模型，其实基本上都会满足无后效性。

- 重复子问题

如果用一句话概括一下，那就是，不同的决策序列，达到某个相同的阶段时，可能会产生重复的状态。所以才会用一个数组记录中间结果，避免重复计算。

## 递归和动态规划关系

递归是一种程序的实现方式：函数的自我调节

```
function(x):
	...
	function(x-1);
	...
```

动态规划：是一种解决问题的思想，大规模问题的结果，是由小规模问题的结果运算得来的。动态规划可用递归来实现（memorization search）

## 使用场景

满足三个条件：最优子结构、无后效性、重复子问题

简单来说就是：

- 满足以下条件之一
  - 求最大/最小值（Maximum/Minimum）
  - 求是否可行（Yes/No）
  - 求可行个数（Count(*)）
- 满足不能排序或者交换（Can not sort/swap）

如题[longest-consecutive-sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence/)  位置可以交换，所以不能用动态规划

## 四点要素

1. 状态 State
   - 灵感，创造力，存储小规模问题的结果
2. 方程 Function
   - 装填之间的联系，怎么通过小的状态，来算大的状态
3. 初始化 Initialization
   - 最极限的小状态是什么，起点
4. 答案 Answer
   - 最大的那个状态是什么，终点

## 常见四种类型

1. Matrix DP (10%)
2. Sequence (40%)
3. Two Sequence DP (40%)
4. Backpack (10%)

> 注意点
>
> - 贪心算法大多题目靠背答案，所以如果能用动态规划就尽量用动态规划，不用贪心算法。

## Matrix DP 矩阵类型 (10%)

### minimum-path-sum

[minimum-path-sum](https://leetcode-cn.com/problems/minimum-path-sum/)

> 
> 给定一个包含非负整数的 *m* x *n* 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
>
> **说明：**每次只能向下或者向右移动一步。

```python
'''
solution: 自顶向下，计算每一个dp矩阵的值。
'''
class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        dp = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                elif i == 0:
                    dp[i][j] = grid[i][j] + dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = grid[i][j] + dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
```

### unique-paths

[unique-paths](https://leetcode-cn.com/problems/unique-paths/)

> 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
>
> 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
>
> 问总共有多少条不同的路径？
>

```Python
'''
solution: 在第一行的第一列移动时，路径的个数并不会变化，到了其他的行列中，每个坐标的路径计算方法为上边的路径和加上左边的路径和。
注意一点初始化方法：dp = [[0] * n] * m 与 dp = [[0 for i in range(n)] for j in range(m)]。第一种方法是得到的结果每一列中所有的值地址都是一样的，所以在赋值时，会同时修改整个列；第二种方法不会发生这种情况，尽量用第二种方法。
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
```

### unique-paths-ii

[unique-paths-ii](https://leetcode-cn.com/problems/unique-paths-ii/)

> 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
>
> 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
>
> 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
>

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i == j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
```

## Sequence 序列类型 (40%)

### climbing-stairs

[climbing-stairs](https://leetcode-cn.com/problems/climbing-stairs/)

> 
> 假设你正在爬楼梯。需要 *n* 阶你才能到达楼顶。
>
> 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
>
> **注意：**给定 *n* 是一个正整数。

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        # n+1是为了防止出现只有一阶台阶的情况
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]
```

### jump-game

[jump-game](https://leetcode-cn.com/problems/jump-game/)

> 给定一个非负整数数组，你最初位于数组的第一个位置。
>
> 数组中的每个元素代表你在该位置可以跳跃的最大长度。
>
> 判断你是否能够到达最后一个位置。

```Python
'''
solution: 用max_position来记录当前可以跳到的最远位置，如果max_position大于序列长度可以直接返回True.在遍历过程中更新能跳到的最远位置，为当前位置加上当前值。如果当前位置小于可以跳到的最远位置，说明怎么也跳不到这里，需要返回False。
'''
class Solution:
    def canJump(self, nums):
        max_position = 0
        for i in range(len(nums)):
            if max_position >= len(nums):
                return True
            if i > max_position:
                return False
            else:
                max_position = max(max_position, nums[i] + i)
        return True
```

### jump-game-ii

[jump-game-ii](https://leetcode-cn.com/problems/jump-game-ii/)

> 给定一个非负整数数组，你最初位于数组的第一个位置。
>
> 数组中的每个元素代表你在该位置可以跳跃的最大长度。
>
> 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
>

```Python
'''
solution: 思想就是挨个挑，同时记录下能跳到的最远距离和当前位置能达到的边界。如果遍历到的位置到达了边界，那就去更新这个边界和更新步数。
'''
class Solution:
    def jump(self, nums):
        max_position = 0
        end = 0
        steps = 0
        for i in range(len(nums) - 1):
            # 在遍历过程中每次都记录可以跳到的最远位置
            max_position = max(max_position, nums[i] + i)
            # 如果当前位置到了边界位置，使用可以跳到的最远位置来进行更新边界，同时更新步数
            if i == end:
                end = max_position
                steps += 1
        return steps
```

### palindrome-partitioning-ii

[palindrome-partitioning-ii](https://leetcode-cn.com/problems/palindrome-partitioning-ii/)

> 给定一个字符串 *s*，将 *s* 分割成一些子串，使每个子串都是回文串。
>
> 返回符合要求的最少分割次数。

```Python
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]
        # 这里借鉴了第5题的思路，使用动态规划在判断是否为回文
        check_palindrome = [[False for _ in range(size)] for _ in range(size)]

        for right in range(size):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or check_palindrome[left + 1][right - 1]):
                    check_palindrome[left][right] = True

        for i in range(1, size):
            if check_palindrome[0][i]:
                dp[i] = 0
                continue
            # 枚举分割点，如果s[0:i]不是回文，那么从s[1:i]开始进行判断，如果是回文就在那个位置的需要切割的次数加1，
            # 最终去最小值就是这个序列需要切割的最小值
            dp[i] = min([dp[j] + 1 for j in range(i) if check_palindrome[j + 1][i]])

        return dp[size - 1]
```

### longest-increasing-subsequence

[longest-increasing-subsequence](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

> 给定一个无序的整数数组，找到其中最长上升子序列的长度。

```Python
'''
solution1: 传统的dp思路，每一个位置的最长上升序列取决于他的上一个位置，依次类推，把问题分割成小问题去解决。定义dp数组，初始值为1，遍历到i位置时，需要将i之前的全部数字看一遍，记录下最长的上升子序列，更新到dp数组中。
solution2: 使用tail数组记录下最长上升子序列，规则为，在遍历数组过程中，如果当前元素大于tail最后一个元素，直接放到tail数组最后，如果小于tail最后一个元素，那么通过二分查找找到第一个比当前元素大于或者等于的数，进行替换，这样就得到了一个结尾更小的相同长度的上升子序列
参考 https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
'''
class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) == 0:
            return 0
        tail = [nums[0]]
        for i in range(1, len(nums)):
            # 如果当前元素比tail最后一个元素大，直接放到tail数组中
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue
            # 如果当前元素比tail数组最后一个元素小，那么通过二分查找进行查找
            # 找到第 1 个大于等于 nums[i] 的元素，尝试让那个元素更小，注意是第一个大于等于num[i]的元素！！！
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) // 2
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = nums[i]
        return len(tail)
```

### word-break

[word-break](https://leetcode-cn.com/problems/word-break/)

> 给定一个**非空**字符串 *s* 和一个包含**非空**单词列表的字典 *wordDict*，判定 *s* 是否可以被空格拆分为一个或多个在字典中出现的单词。

```Python
'''
solution: 初始化dp数组全为false，并且有n+1个，因为第一个要初始化为True，dp[i]代表前i个元素可以拆分为字典中的词。在遍历过程中，考虑如下问题，以当前元素为i终点，以i之前的任意位置j为起点是否在字典中，并且dp[j]是否为True，如果dp[j]为True，说明前j个元素可以用字典表示，并且s[j:i]也在字典中，说明前i个元素可以用字典表示。
'''
class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
```

## Two Sequence 两个序列类型（40%） 

### longest-common-subseqence

[longest-common-subsequence](https://leetcode-cn.com/problems/longest-common-subsequence/)

> 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
>
> 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
> 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
>
> 若这两个字符串没有公共子序列，则返回 0。
>

```python 
'''
solution: 定义一个dp数组，每个位置所代表的元素，dp[i][j]为text1[0:i]与text2[0:j]之间最大的公共子序列。那么状态转移就很好解决了，如果当前元素相同，那么就是在上一个状态上加1就好，如果不想相同，只需要判断dp[i-1][j]与dp[i][j-1]哪个大就好了。这个过程可以参考递归的代码来理解。
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def longestCommonSubsequence_recursion(self, text1, text2):
        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                return dp(i - 1, j - 1) + 1
            else:
                return max(dp(i - 1, j), dp(i, j - 1))

        return dp(len(text1) - 1, len(text2) - 1)
```

### edit-distance

[edit-distance](https://leetcode-cn.com/problems/edit-distance/)

```Python
'''
solution 使用动态规划。由后往前去看，如果两个字符串的最后一位相同，那么直接对比word1的前i-1与word2的前j-1位；如果最后一位不同的话，这里有三种方法进行操作，计算分别使用这三种方法后，哪种方法所需的步数最少。状态矩阵可以这么想，dp[i][j]的意思就是，将word1的i个字符转换成word2的j个字符，那么下边的这三种操作就不难理解：
dp[i][j - 1] 插入操作，将word1的前i个字符变为word2的前j-1个字符，即在word1后插入一个与word2最后第j个字符相同的字符；
dp[i - 1][j] 删除操作，将word1的前i-1个字符变为word2的前j个字符；
dp[i - 1][j - 1] 替换操作，将word1的前i-1个字符变为word2的前j-1个字符，即将word1最后一个字符替换成word2的最后一个字符。
'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        # 如果word1为空，那么由word1变为word2所需要的步数
        for j in range(1, l2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        # 如果word2为空，那么由word1变为word2所需要的步数
        for i in range(1, l1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
```

### 总结

一般找子串问题，都是使用动态规划来解决。

对于两个字符串的动态规划问题，一般都是定义dp table，这样可以很容易写出动态转换方程，只要做好选择就好。

![img](https://pic.leetcode-cn.com/be4d0c3b1a9e9f594c4498a666fa63359f690324bd5605f1896bb4f6fdb2762b.png)

## Backpack 零钱和背包 (10%)

### coin-change

[coin-change](https://leetcode-cn.com/problems/coin-change/)

> 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
>

```Python
'''
solution: 动态规划的思想就是，想要解决fn(5)，那么就要先解决fn(4)，依次类推，那么这里dp数组就定义amount为n时的解为多少。
动态转移矩阵就是，min(dp[i], dp[i - coin] + 1)
'''
class Solution:
    def coinChange(self, coins, amount) -> int:
        # 初始化dp数组为amount+1，硬币个数最多为amount个，所以大于amount就是一个无意义的数。
        dp = [amount + 1 for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]
```

### backpack

[backpack](https://www.lintcode.com/problem/backpack/description)

> 在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

```Python
'''
solution: 使用dp记录每个容量是够可以凑齐，然后选出最大的可以凑齐的容量就是结果。首先将背包中第一个元素在dp数组中设置为True，因为如果这个元素小于背包总容量的话，那么他所代表的容量就能凑齐。然后从第二个元素开始遍历背包内的元素，内层循环为，背包总容量减去当前遍历的元素，看背包中剩下的元素谁能凑齐这些容量，如果凑齐，那么dp[j + A[i]] = True. 原因是dp[j]可以凑齐，dp[A[i]]也可以凑齐，那么他俩相加的容量肯定也能凑齐。
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """

    def backPack(self, m, A):
        # write your code here
        n = len(A)
        dp = [False for _ in range(m + 1)]
        dp[0] = True
        if A[0] <= m:
            dp[A[0]] = True
        # 遍历背包元素
        for i in range(1, n):
            # 从背包容留减去当前遍历到的元素A[i]开始进行遍历，这个就是当前最大容量。
            # 如果dp数组中已经有可以凑齐当前值dp[j]的元素，那么这两个和肯定也能凑齐。
            for j in range(m - A[i], -1, -1):
                if dp[j] == True:
                    dp[j + A[i]] = True
        # 从最大容量开始遍历，如果为True，说明可以凑齐，然后返回，如果一直没有返回说明不能凑齐。
        for i in range(m, -1, -1):
            if dp[i] == True:
                return i

        return 0
```

### backpack-ii

[backpack-ii](https://www.lintcode.com/problem/backpack-ii/description)

> 有 `n` 个物品和一个大小为 `m` 的背包. 给定数组 `A` 表示每个物品的大小和数组 `V` 表示每个物品的价值.
>
> 问最多能装入背包的总价值是多大?

```Python
'''
solution: 01背包问题，定义背包容量大小的dp数组，记录每一个容量能取得的最大价值。动态转移方程为：如果将当前元素添加到背包中，那么新的总价值为dp[当前容量-当前元素大小] + 当前元素价值；如果不添加当前元素，那么价值为dp[当前容量]。选择最大的即可。
另外，可以将该方法进行封装，在一系列背包问题中都可以使用。
'''
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """

    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        dp = [0 for _ in range(m + 1)]
        # 遍历每一个元素的大小
        for i in range(n):
            # 从背包容量开始遍历到当前元素的大小
            for v in range(m, A[i] - 1, - 1):
                # 将当前元素加到背包中，与不添加该元素，哪一个价值更高选哪个
                dp[v] = max(dp[v], dp[v - A[i]] + V[i])

        return dp[m]

    def backPackII_2(self, m, A, V):
        n = len(A)
        if n == 0:
            return 0
        dp = [0 for i in range(m + 1)]

        # 将该思路封装，在其他背包问题中可以进行使用
        def zero_one_backpack(dp, m, A, V):
            for v in range(m, A - 1, -1):
                dp[v] = max(dp[v], dp[v - A] + V)

        for i in range(n):
            zero_one_backpack(dp, m, A[i], V[i])
        return dp[m]
```

