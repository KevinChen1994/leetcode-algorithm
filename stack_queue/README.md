# 栈和队列

## 简介

栈：先进后出。根据这个特点可以临时保存一些数据，之后用到在依次弹出来，常用于DFS。

队列：先进先出。常用于BFS，类似于一层一层的搜索。

## stack

### min-stack

[min-stack](https://leetcode-cn.com/problems/min-stack/)

> 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
>
> - push(x) —— 将元素 x 推入栈中。
> - pop() —— 删除栈顶的元素。
>
> - top() —— 获取栈顶元素。
> - getMin() —— 检索栈中的最小元素。

```python
'''
solution: 使用两个栈，一个栈存放数据，另外一个栈存放最小值
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float('inf')]
        self.min = float('inf')

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min = min(self.min, x)
        self.min_stack.append(self.min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min = self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

### evaluate-reverse-polish-natation

[evaluate-reverse-polish-notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)

> 根据 逆波兰表示法，求表达式的值。
>
> 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。
>
> 说明：
>
> - 整数除法只保留整数部分。
> - 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

```python
class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num2 / num1))
            else:
                stack.append(int(token))
        return stack[-1]


if __name__ == '__main__':
    solution = Solution()
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(solution.evalRPN(tokens))
```

### decode-string

[decode-string](https://leetcode-cn.com/problems/decode-string/)

> 给定一个经过编码的字符串，返回它解码后的字符串。
>
> 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
>
> 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
>
> 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
>

```python
'''
solution1: 使用栈存储要翻的倍数和翻倍之前的结果。
solution2: 递归。
'''

class Solution:
    def decodeString_1(self, s: str) -> str:
        num = 0
        result = ''
        stack = []
        for w in s:
            if '0' <= w <= '9':
                num = num * 10 + int(w)
            elif w == '[':
                stack.append([num, result])
                num = 0
                result = ''
            elif w == ']':
                cur_num, last_res = stack.pop()
                result = last_res + cur_num * result
            else:
                result += w
        return result

    def decodeString_2(self, s):
        def dfs(s, i):
            res, num = '', 0
            # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
            while i < len(s):
                if '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                elif s[i] == '[':
                    # 注意，返回i的含义是更新上层递归指针位置，因为内层递归已经吃掉一串str，若不更新i，外层仍然从i+1开始，则会重复处理内层处理过的一串str。
                    i, tmp = dfs(s, i + 1)
                    res += num * tmp
                    num = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


if __name__ == '__main__':
    solution = Solution()
    s = '3[a2[c]]'
    print(solution.decodeString_1(s))
```

### binary-tree-inorder-traversal

[binary-tree-inorder-traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

> 给定一个二叉树，返回它的*中序* 遍历。

```python
class Solution:
    def inorderTraversal(self, root: TreeNode):

        result = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
```

### clone-graph

[clone-graph](https://leetcode-cn.com/problems/clone-graph/)

> 给你无向 **[连通](https://baike.baidu.com/item/连通图/6460995?fr=aladdin)** 图中一个节点的引用，请你返回该图的 [**深拷贝**](https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin)（克隆）。

```python
# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph_1(self, node: 'Node') -> 'Node':
        from _collections import deque
        # lookup中存放新创建的节点，也就是复制的节点
        lookup = {}

        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            lookup[node] = clone
            queue = deque()
            queue.appendleft(node)
            while queue:
                tmp = queue.pop()
                for n in tmp.neighbors:
                    if n not in lookup:
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)
                    lookup[tmp].neighbors.append(lookup[n])
            return clone

        return bfs(node)

    def cloneGraph_2(self, node):
        lookup = {}

        def dfs(node):
            if not node:
                return node
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)
```

### number-of-islands

[number-of-islands](https://leetcode-cn.com/problems/number-of-islands/)

> 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
>
> 岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
>
> 此外，你可以假设该网格的四条边均被水包围。
>

```python
'''
solution1: dfs，一直沿着一个方向找，直到遇到为0的点，会换个方向，然后再沿着一个方向找，直到把整个岛屿标记完。
solution2: bfs，借用队列实现，一个点先沿着他周边四个方向找，把周边的四个方向全部验证一遍，之后在到另外一个点，继续验证四个方向，直到把整个岛屿标记完。
'''
class Solution:
    def numIslands_1(self, grid):
        result = 0
        # 左、下、右、上
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        if m == 0:
            return result
        n = len(grid[0])
        marked = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] is False:
                    result += 1
                    self.dfs(i, j, m, n, marked, grid)
        return result

    def dfs(self, i, j, m, n, marked, grid):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == '1' and marked[new_i][new_j] is False:
                self.dfs(new_i, new_j, m, n, marked, grid)

    def numIslands_2(self, grid):
        from _collections import deque
        result = 0
        # 左、下、右、上
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        m = len(grid)
        if m == 0:
            return result
        n = len(grid[0])
        marked = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and marked[i][j] is False:
                    result += 1
                    queue = deque()
                    queue.appendleft((i, j))
                    while queue:
                        cur_i, cur_j = queue.pop()
                        for direction in directions:
                            new_i = cur_i + direction[0]
                            new_j = cur_j + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and marked[new_i][new_j] is False and grid[new_i][
                                new_j] == '1':
                                marked[new_i][new_j] = True
                                queue.appendleft((new_i, new_j))
        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    print(solution.numIslands_2(grid))
```

### largest-rectangle-in-histogram

[largest-rectangle-in-histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)

> 给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
>
> 求在该柱状图中，能够勾勒出来的矩形的最大面积。

```python
'''
solution: 如果用暴力法很好解决，就是在遍历过程中，每个高度分别往左往右找到第一个比他小的数，在以当前元素为高，两个比他小的数为之间的长度为宽，进行相乘就是面积。这里可以借助栈降低时间复杂度，用空间换时间。在遍历过程中，将大于当前元素的索引压入栈中，这样栈内的索引都是按照实际值的从小到大的顺序的，这样方便计算，接下来在遍历过程中，如果遇到元素比栈顶元素小，这时就要以栈顶元素所代表的元素为高进行计算面积了，高确定了，那么宽就是当前元素索引减去弹出栈顶后下一个索引的差再减去1，具体原因为这两个索引分别是栈顶元素左边和右边第一个比他小的数，索引相减在减一是实际的宽度。
'''
class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            # 如果栈内索引所代表的元素大于当前元素，这时候就要以这个索引所代表的元素的高度计算面积了
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                # 面积计算公式：栈顶元素的高度*（两边元素的索引-1），两边的索引都是第一个比当前元素小的索引。
                max_area = max(max_area, heights[tmp] * (i - stack[-1] - 1))
            # 只有当前元素比栈顶元素大时才入栈，所以栈内元素都是从小到大进行排序的
            stack.append(i)
        return max_area

if __name__ == '__main__':
    solution = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(solution.largestRectangleArea(heights))
```

