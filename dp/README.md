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

