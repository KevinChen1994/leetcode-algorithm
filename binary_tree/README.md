# 二叉树

## 二叉树遍历
前序遍历：根节点-左子树-右子树

中序遍历：左子树-根节点-右子树

后续遍历：左子树-右子树-根节点

### 树结构：
``` python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
```

### 前序遍历
```python
def preOrderRecursive(root):
    if not root:
        return
    print(root.val)
    preOrderRecursive(root.left)
    preOrderRecursive(root.right)
```

### 中序遍历
```python
def inOrderRecursive(root):
    if not root:
        return
    inOrderRecursive(root.left)
    print(root.val)
    inOrderRecursive(root.right)
```

### 后序遍历
```python
def postOrderRecursive(root):
    if not root:
        return
    postOrderRecursive(root.left)
    postOrderRecursive(root.right)
    print(root.val)
```

### 前序非递归遍历
```python
def preOrderRecursive(root):
    stack = [root]
    while root:
        print(root.val)
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
        root = stack.pop()
```

### 中序遍历非递归
先遍历到最左边的左子树，然后往上层层回溯
```python
def InOrderRecursive(root):
    stack = []
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.val)
            root = root.right
```

### 后序遍历非递归
与前序遍历类似，不过进栈顺序(stack1)是根节点-左子树-右子树，出栈顺序是根节点-右子树-左子树，每次stack1出栈，都会进栈到stack2中，那么最终stack2出栈顺序就是左子树-右子树-根节点
```python
def PostOrderRecursive(root):
    stack1 = [root]
    stack2 = []
    while stack1:
        root = stack1.pop()
        stack2.append(root)
        if root.left:
            stack1.append(root.left)
        if root.right:
            stack1.append(root.right)
    while stack2:
        print(stack2.pop().val)
```

### DFS，从上到下
对于[1,2,3,4,5,6,7]二叉树，输出是[1,2,4,5,3,6,7]
```python
class Solution:
    def dfsUp2Down(self, root):

        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)

        res = []
        dfs(root, res)
        return res
```

### DFS，从下到上(分治法)
```python
class Solution:
    def preOrderTraversal(self, root):
        return self.divideAndConquer(root)

    def divideAndConquer(self, root):
        result = []
        if not root:
            return None
        left = self.divideAndConquer(root.left)
        right = self.divideAndConquer(root.right)
        result.append(root.val)
        if left is not None:
            result += left
        if right is not None:
            result += right
        return result
```

### BFS层次遍历

```python
def levelOrder(root):
    if not root:
        return None
    queue = [root]
    while queue:
        root = queue.pop(0)
        print(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
```

## 分治法应用

先分别处理局部，再合并结果

适用场景

- 快排
- 归并排序
- 二叉树相关问题

分治法模板

- 递归返回条件
- 分段处理
- 合并结果

```python
# 伪代码
class Solution:
  def traversal(root):
    if not root:
      # do something
   	# divide
    left = traversal(root.left)
    right = traversal(root.right)
    # conquer
    result = Merge from left and right
    
    return result
    
```

### 典型示例

```python
# 分治法遍历二叉树
class Solution:
    def preOrderTraversal(self, root):
        return self.divideAndConquer(root)

    def divideAndConquer(self, root):
        result = []
        if not root:
            return None
        left = self.divideAndConquer(root.left)
        right = self.divideAndConquer(root.right)
        result.append(root.val)
        if left is not None:
            result += left
        if right is not None:
            result += right
        return result
```

### 归并排序

```python
# Time complexity O(nlogn)
class Solution:
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        # 分治
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):
        # 将left 和 right合并成一个有序的数组
        l, r = 0, 0
        new_list = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                new_list.append(left[l])
                l += 1
            else:
                new_list.append(right[r])
                r += 1
        new_list += left[l:]
        new_list += right[r:]
        return new_list
```

### 快排

```Python
# Time complexity O(nlogn)
class Solution:
    def quick_sort(self, nums, left, right):
        if left < right:
            # 求出分割点pivot，pivot左边小于pivot右边
            pivot = self.partition(nums, left, right)
            # 每轮排序后，pivot的位置都是固定的，后续不会再更改
            self.quick_sort(nums, left, pivot - 1)
            self.quick_sort(nums, pivot + 1, right)

    def partition(self, nums, left, right):
        # 以最后一个元素作为目标值，在遍历过程中，如果当前元素小于target，就与i进行交换，同时i增加1。
        target = nums[right]
        i = left - 1
        for j in range(left, right):
            if nums[j] < target:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        # 最后再把最后一位移到i+1个位置，此时i + 1就是分割点
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1
```

注意点

> 快排是在原数组进行交换，所以没有合并过程。
>
> 传入的索引是存在的索引，注意不要数组越界。

### maximum-depth-of-binary-tree

[maximum-depth-of-binary-tree](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)

> 给定一个二叉树，找出其最大深度。

```python
class Solution:
  def maxDepth(tree):
    if not root:
      return 0
    left = self.maxDepth(tree.left)
    right = self.maxDepth(tree.right)
    return max(left, right) + 1
```

### balanced-binary-tree

[balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree/)

> 给定一个二叉树，判断它是否是一个高度平衡的二叉树。高平衡的二叉树定义：一个二叉树*每个节点* 的左右两个子树的高度差的绝对值不超过1。

```python
'''
solution1: 高度平衡二叉树需要满足：左子树是高度平衡二叉树；右子树是高度平衡二叉树；左右子树深度差值不能大于1.isBalanced()会遍历整个二叉树，时间复杂度是O(N),depth()需要遍历各子树的所有结点，时间复杂度是O(logN),所以最终时间复杂度是O(NlogN)
solution2: 使用一个全局变量记录状态，如果有一棵子树不是高度平衡二叉树，那么整个数也就不是。需要遍历整个子树，时间复杂度为O(N)
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def isBalanced_1(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced_1(root.left) and self.isBalanced_1(root.right) and abs(
            self.depth(root.left) - self.depth(root.right)) <= 1

    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced_2(self, root):
        self.result = True
        self.max_depth(root)
        return self.result

    def max_depth(self, root):
        if not root:
            return 0
        left = self.max_depth(root.left)
        right = self.max_depth(root.right)
        if abs(left - right) > 1:
            self.result = False
        return max(left, right) + 1
```

### binary-tree-maximum-path-sum

[binary-tree-maximum-path-sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/)

> 给定一个**非空**二叉树，返回其最大路径和。

```python
'''
solution: 分治思想，递归计算出左右节点分别的贡献值，只有当贡献值大于0时才使用这条路径。结点的贡献值取决于当前结点的值和他的左右节点的贡献值，每次递归返回该节点的最大贡献值。时间复杂度O(N)，对每个节点只访问一次。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_result = float('-inf')
        self.maxContribution(root)
        return self.max_result

    # 返回结点的最大贡献值，并且在遍历过程中记录最大的路径和
    def maxContribution(self, root):
        if not root:
            return 0
        # 只保留左右节点大于0的贡献值。
        left = max(self.maxContribution(root.left), 0)
        right = max(self.maxContribution(root.right), 0)
        # 节点路径和取决于当前节点和他左右节点的最大贡献值
        self.max_result = max(self.max_result, root.val + left + right)
        # 返回该节点的贡献值
        return root.val + max(left, right)
```

### lowest-common-ancestor-of-a-binary-tree

[lowest-common-ancestor-of-a-binary-tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)

> 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。**一个节点也可以是它自己的祖先**

```python
'''
solution: 如果公共祖先在左子树就返回左子树，如果公共祖先在右子树就返回右子树，否则返回根节点。时间复杂度O(N)。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

## BFS应用

### binary-tree-level-order-traversal

[binary-tree-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)

> 给你一个二叉树，请你返回其按 **层序遍历** 得到的节点值。 （即逐层地，从左到右访问所有节点）。

```python
'''
solution: 使用队列记录每一层的节点，遍历当前队列的大小次，每次遍历当前队列中的节点。一个数进去一次出来一次，时间复杂度O(logN)
'''
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            tmp_list = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp_list.append(node.val)
            result.append(tmp_list)
        return result
```

### binary-tree-level-order-traversal-ii

[binary-tree-level-order-traversal-ii](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/)

> 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

```python
'''
solution: 跟正序层次遍历二叉树一样的流程，不过在插入result的时候每次都插到最左边。另外还可以直接按照正序层次遍历二叉树，最后结果result[::-1]，直接翻转结果，这是Python的特性，不过这样很慢，这个操作时间复杂度有点高。
'''
    def levelOrserBotton(self, root):
        result = []
        if not root:
            return result
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for i in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.insert(0, tmp)
        return result
```

### binary-tree-zigzag-level-order-traversal

[binary-tree-zigzag-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/)

```python
'''
solution: 设置一个flag，是True的时候就将结果从左到右输出到数组中，False的话就从右到左输出到数组中。
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        result = []
        if not root:
            return result
        queue = [root]
        flag = True
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if flag:
                    tmp.append(node.val)
                else:
                    tmp.insert(0, node.val)
            flag = False if flag else True
            result.append(tmp)
        return result
```

## 二叉搜索树应用

