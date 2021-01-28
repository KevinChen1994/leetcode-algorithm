# 题目列表
感谢[花花酱](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) 的分享，将题目按照不同的类别进行分组，并且有难度、相似题目和一些技巧。花花酱在YouTube和B站都有分享解题思路，非常硬核。

## DP

| ID   | name                                                         | Difficulty | Similar Problems                 | Comments                                                     |
| :--- | ------------------------------------------------------------ | ---------- | -------------------------------- | ------------------------------------------------------------ |
| 730  | [Count Different Palindromic Subsequences](https://leetcode-cn.com/problems/count-different-palindromic-subsequences/) | Hard       |                                  |                                                              |
| 978  | [Longest Turbulent Subarray](https://leetcode-cn.com/problems/longest-turbulent-subarray/) | Hard       |                                  |                                                              |
| 70   | [Climbing Stairs](https://leetcode-cn.com/problems/climbing-stairs/) | Easy       | 746、1137                        |                                                              |
| 746  | [Min Cost Climbing Stairs](https://leetcode-cn.com/problems/min-cost-climbing-stairs/) | Easy       |                                  |                                                              |
| 1137 | [N-th Tribonacci Number](https://leetcode-cn.com/problems/n-th-tribonacci-number/) | Easy       |                                  |                                                              |
| 303  | [Range Sum Query Immutable](https://leetcode-cn.com/problems/range-sum-query-immutable/) |            | 1218                             |                                                              |
| 1218 | [Longest Arithmetic Subsequence Of Given Difference](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/) |            |                                  |                                                              |
| 53   | [Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/) | Easy       | 121                              |                                                              |
| 121  | [Best Time To Buy And Sell Stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | Easy       |                                  |                                                              |
|      |                                                              |            |                                  |                                                              |
|      |                                                              |            |                                  |                                                              |
| 72   | [Edit Distance](https://leetcode-cn.com/problems/edit-distance/) | Hard       | 1458、10、44、97、115、712、1187 | 这种都需要分各种情况，一定要分清楚再去写状态转移方程。       |
| 1458 | [Max Dot Product Of Two Subsequences](https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences/) | Hard       |                                  |                                                              |
| 10   | [Regular Expression Matching](https://leetcode-cn.com/problems/regular-expression-matching/) | Hard       |                                  |                                                              |
| 44   | [Wildcard Matching](https://leetcode-cn.com/problems/wildcard-matching/) | Hard       |                                  | 与第10题相比，稍微简单了一点。                               |
| 97   | [Interleaving String](https://leetcode-cn.com/problems/interleaving-string/) | Hard       |                                  | 这类题目不要忘记首先定义好初始状态，有时候不只有dp[[0]][][0]才是True，需要考虑全所有的初始状态，例如：10中的需要判断如果开头是.*的需要将dp矩阵设置到他所代表的位置；97中需要提前定义好s3是s1还是s2谁先来组成的。 |
| 115  | [Distinct Subsequences](https://leetcode-cn.com/problems/distinct-subsequences/) | Hard       |                                  |                                                              |
| 712  | [Minimum ASCII Delete Sum For Two Strings](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/) | Medium     |                                  |                                                              |
| 1187 | [Make Array Strictly Increasing](https://leetcode-cn.com/problems/make-array-strictly-increasing/) | Hard       |                                  | 太难了，做了一天！                                           |
| 1143 | [Longest Common Subsequence](https://leetcode-cn.com/problems/longest-common-subsequence/) | Medium     |                                  | 很经典的一道题，做过前边几道题，看到这道题就很简单了。       |
| 1092 | [Shortest Common Supersequence](https://leetcode-cn.com/problems/shortest-common-supersequence/) | Hard       |                                  |                                                              |
| 718  | [Maximum Length Of Repeated Subarray](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/) | Medium     |                                  |                                                              |
|      |                                                              |            |                                  |                                                              |

##LinkedList

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 24   | [Swap Nodes In Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | Medium     | 25、206          |          |
| 25   | [Reverse Nodes In K Group](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) | Hard       |                  |          |
| 206  | [Reverse Linked List](https://leetcode-cn.com/problems/reverse-linked-list/) | Easy       |                  |          |
| 2    | [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/) | Medium     | 445              |          |
| 445  | [Add Two Numbers II](https://leetcode-cn.com/problems/add-two-numbers-ii/) | Medium     |                  |          |
|      |                                                              |            |                  |          |
|      |                                                              |            |                  |          |
|      |                                                              |            |                  |          |
|      |                                                              |            |                  |          |

## HashTable

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 1    | [Two Sum](https://leetcode-cn.com/problems/two-sum/)         | Easy       | 560              |          |
| 560  | [Subarray Sum Equals K](https://leetcode-cn.com/problems/subarray-sum-equals-k/) |            |                  |          |
|      |                                                              |            |                  |          |

## TwoPointers

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 15   | [3Sum](https://leetcode-cn.com/problems/3sum/)               | Medium     | 16、167          |          |
| 16   | [3Sum Closest](https://leetcode-cn.com/problems/3sum-closest/) | Medium     |                  |          |
| 167  | [Two Sum II Input Array Is Sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | Easy       |                  |          |

### Tree

| ID   | name                                                         | Difficulty | Similar Problems | Comments                     |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | ---------------------------- |
| 94   | [Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | Medium     | 144、145         | 使用递归和辅助栈两种方法实现 |
| 144  | [Binary Tree Preorder Traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) | Medium     |                  |                              |
| 145  | [Binary Tree Postorder Traversal](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) | Medium     |                  |                              |
| 102  | [Binary Tree Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) | Medium     | 107、103         |                              |
| 107  | [Binary Tree Level Order Traversal II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/) | Easy       |                  |                              |
| 103  | [Binary Tree Zigzag Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium     |                  |                              |

### Graph

| ID   | name                                                         | Difficulty | Similar Problems         | Comments                                             |
| ---- | ------------------------------------------------------------ | ---------- | ------------------------ | ---------------------------------------------------- |
| 133  | [Clone Graph](https://leetcode-cn.com/problems/clone-graph/) | Medium     | 138                      | DFS                                                  |
| 138  | [Copy List With Random Pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer/) | Medium     |                          |                                                      |
| 200  | [Number Of Islands](https://leetcode-cn.com/problems/number-of-islands/) | Medium     | 547、695、733、827、1162 | DFS                                                  |
| 547  | [Number Of Provinces](https://leetcode-cn.com/problems/number-of-provinces/) | Medium     |                          | 在美国站中这道题叫朋友圈，只是改了个名字，思路一样。 |
| 695  | [Max Area Of Island](https://leetcode-cn.com/problems/max-area-of-island/) | Medium     |                          |                                                      |
| 733  | [Flood Fill](https://leetcode-cn.com/problems/flood-fill/)   | Easy       |                          |                                                      |
| 827  | [Making A Large Island](https://leetcode-cn.com/problems/making-a-large-island/) | Hard       |                          | 这道题是一道变型题，挺有意思的。                     |
| 1162 | [As Far From Land As Possible](https://leetcode-cn.com/problems/as-far-from-land-as-possible/) | Medium     |                          | BFS                                                  |
|      |                                                              |            |                          |                                                      |
|      |                                                              |            |                          |                                                      |
|      |                                                              |            |                          |                                                      |

