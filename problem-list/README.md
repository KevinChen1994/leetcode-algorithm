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
| 303  | [Range Sum Query Immutable](https://leetcode-cn.com/problems/range-sum-query-immutable/) | Easy       | 1218                             |                                                              |
| 1218 | [Longest Arithmetic Subsequence Of Given Difference](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/) | Medium     |                                  |                                                              |
| 53   | [Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/) | Easy       | 121                              |                                                              |
| 121  | [Best Time To Buy And Sell Stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | Easy       |                                  |                                                              |
| 62   | [Uique-Paths](https://leetcode-cn.com/problems/unique-paths/) | Medium     | 63、64、120、174、931、1210      | 这类题目需要确定好路径是怎么进行的，就是当前位置可以哪些位置到达，依次判断可以到达的路径即可。 |
| 63   | [Unique Paths II](https://leetcode-cn.com/problems/unique-paths-ii/) | Medium     |                                  |                                                              |
| 64   | [Minimum Path Sum](https://leetcode-cn.com/problems/minimum-path-sum/) | Medium     |                                  |                                                              |
| 120  | [Triangle](https://leetcode-cn.com/problems/triangle/)       | Medium     |                                  |                                                              |
| 174  | [Dungeon Game](https://leetcode-cn.com/problems/dungeon-game/) | Hard       |                                  |                                                              |
| 931  | [Minimum Falling Path Sum](https://leetcode-cn.com/problems/minimum-falling-path-sum/) | Medium     |                                  |                                                              |
| 1210 | [Minimum Moves To Reach Target With Rotations](https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations/) |            |                                  |                                                              |
| 85   | [Maximal Rectangle](https://leetcode-cn.com/problems/maximal-rectangle/) | Hard       | 221、304、1277                   | 定义好dp状态转换，相对容易一些。                             |
| 221  | [Maximal Square](https://leetcode-cn.com/problems/maximal-square/) | Medium     |                                  |                                                              |
| 304  | [Range Sum Query 2D Immutable](https://leetcode-cn.com/problems/range-sum-query-2d-immutable/) |            |                                  |                                                              |
| 1277 | [Count Square Submatrices With All Ones](https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/) | Medium     |                                  |                                                              |
| 198  | [House Robber](https://leetcode-cn.com/problems/house-robber/) | Medium     | 213、309、740、790、801          |                                                              |
| 213  | [House Robber II](https://leetcode-cn.com/problems/house-robber-ii/) | Medium     |                                  | 将原数组进行分割，转换成198                                  |
| 309  | [Best Time To Buy And Sell Stock With Cooldown](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium     |                                  |                                                              |
| 740  | [Delete And Earn](https://leetcode-cn.com/problems/delete-and-earn/) | Medium     |                                  | 转换为打家劫舍                                               |
| 790  | [Domino And Tromino Tiling](https://leetcode-cn.com/problems/domino-and-tromino-tiling/) | Medium     |                                  |                                                              |
| 801  | [Minimum Swaps To Make Sequences Increasing](https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing/) | Medium     |                                  |                                                              |
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

## LinkedList

| ID   | name                                                         | Difficulty | Similar Problems | Comments                                                     |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | ------------------------------------------------------------ |
| 2    | [Add Two Numbers](https://leetcode-cn.com/problems/add-two-numbers/) | Medium     | 445              |                                                              |
| 445  | [Add Two Numbers II](https://leetcode-cn.com/problems/add-two-numbers-ii/) | Medium     |                  |                                                              |
| 24   | [Swap Nodes In Pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs/) | Medium     | 25、206          |                                                              |
| 25   | [Reverse Nodes In K Group](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) | Hard       |                  |                                                              |
| 206  | [Reverse Linked List](https://leetcode-cn.com/problems/reverse-linked-list/) | Easy       | 92               |                                                              |
| 92   | [Reverse Linked List II](https://leetcode-cn.com/problems/reverse-linked-list-ii/) | Medium     |                  |                                                              |
| 141  | [Linked List Cycle](https://leetcode-cn.com/problems/linked-list-cycle/) | Easy       | 142              |                                                              |
| 142  | [Linked List Cycle II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) | Medium     |                  |                                                              |
| 21   | [Merge Two Sorted Lists](https://leetcode-cn.com/problems/merge-two-sorted-lists/) | Easy       | 23               |                                                              |
| 23   | [Merge K Sorted Lists](https://leetcode-cn.com/problems/merge-k-sorted-lists/) | Hard       |                  | 归并                                                         |
| 160  | [Intersection Of Two Linked Lists](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) | Easy       |                  | 相同路程，两个人速度相同，即使起点不同，最终也是同时到终点。 |
|      |                                                              |            |                  |                                                              |

## HashTable

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 1    | [Two Sum](https://leetcode-cn.com/problems/two-sum/)         | Easy       | 560              |          |
| 560  | [Subarray Sum Equals K](https://leetcode-cn.com/problems/subarray-sum-equals-k/) |            |                  |          |
|      |                                                              |            |                  |          |

## TwoPointers

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 11   | [Container With Most Water](https://leetcode-cn.com/problems/container-with-most-water/) | Medium     | 42               |          |
| 42   | [Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/) | Hard       |                  |          |
| 167  | [Two Sum II Input Array Is Sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/) | Easy       | 15、16           |          |
| 15   | [3Sum](https://leetcode-cn.com/problems/3sum/)               | Medium     |                  |          |
| 16   | [3Sum Closest](https://leetcode-cn.com/problems/3sum-closest/) | Medium     |                  |          |
| 88   | [Merge Sorted Array](https://leetcode-cn.com/problems/merge-sorted-array/) | Easy       |                  |          |

## Tree

| ID   | name                                                         | Difficulty | Similar Problems             | Comments                                    |
| ---- | ------------------------------------------------------------ | ---------- | ---------------------------- | ------------------------------------------- |
| 94   | [Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | Medium     | 144、145                     | 使用递归和辅助栈两种方法实现                |
| 144  | [Binary Tree Preorder Traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) | Medium     |                              |                                             |
| 145  | [Binary Tree Postorder Traversal](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) | Medium     |                              |                                             |
| 100  | [Same Tree](https://leetcode-cn.com/problems/same-tree/)     | Easy       | 101、104、110、111、572、965 |                                             |
| 101  | [Symmetric Tree](https://leetcode-cn.com/problems/symmetric-tree/) | Easy       |                              |                                             |
| 104  | [Maximum Depth Of Binary Tree](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) | Easy       |                              |                                             |
| 110  | [Balanced Binary Tree](https://leetcode-cn.com/problems/balanced-binary-tree/) | Easy       |                              |                                             |
| 111  | [Minimum Depth Of Binary Tree](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/) | Easy       |                              |                                             |
| 572  | [Subtree Of Another Tree](https://leetcode-cn.com/problems/subtree-of-another-tree/) | Easy       |                              |                                             |
| 965  | [Univalued Binary Tree](https://leetcode-cn.com/problems/univalued-binary-tree/) | Easy       |                              |                                             |
| 102  | [Binary Tree Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) | Medium     | 107、103                     |                                             |
| 107  | [Binary Tree Level Order Traversal II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/) | Easy       |                              |                                             |
| 103  | [Binary Tree Zigzag Level Order Traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/) | Medium     |                              |                                             |
| 236  | [Lowest Common Ancestor Of A Binary Tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium     | 235                          |                                             |
| 235  | [Lowest Common Ancestor Of A Binary Search Tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Easy       |                              |                                             |
| 199  | [Binary Tree Right Side View](https://leetcode-cn.com/problems/binary-tree-right-side-view/) | Medium     |                              | 层次遍历                                    |
| 297  | [Serialize And Deserialize Binary Tree](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) | Hard       | 449                          |                                             |
| 449  | [Serialize And Deserialize BST](https://leetcode-cn.com/problems/serialize-and-deserialize-bst/) | Medium     |                              | 这道题比297有意思，需要考虑二叉搜索树的性质 |
| 508  | [Most Frequent Subtree Sum](https://leetcode-cn.com/problems/most-frequent-subtree-sum/) | Medium     |                              | DFS                                         |
| 124  | [Bnary Tree Maximum Path Sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/) | Hard       | 543、687                     |                                             |
| 543  | [Diameter Of Binary Tree](https://leetcode-cn.com/problems/diameter-of-binary-tree/) | Easy       |                              |                                             |
| 687  | [Longest Univalue Path](https://leetcode-cn.com/problems/longest-univalue-path/) | Medium     |                              |                                             |
| 105  | [Construct Binary Tree From Preorder And Inorder Traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium     | 106、889、1008               |                                             |
| 106  | [Cnstruct Binary Tree From Inorder And Postorder Traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Medium     |                              |                                             |
| 889  | [Construct Binary Tree From Preorder And Postorder Traversal/](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | Medium     |                              |                                             |
| 1008 | [Construct Binary Search Tree From Preorder Traversal](https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal/) | Medium     |                              |                                             |

## Graph

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

## Search

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 215  | [Kth Largest Element In An Array](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | Medium     |                  |          |
|      |                                                              |            |                  |          |
|      |                                                              |            |                  |          |

## String

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 415  | [Add Strings](https://leetcode-cn.com/problems/add-strings/) | Easy       |                  |          |
|      |                                                              |            |                  |          |
|      |                                                              |            |                  |          |

## Binary Search

| ID   | name                                             | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------ | ---------- | ---------------- | -------- |
| 69   | [Sqrtx](https://leetcode-cn.com/problems/sqrtx/) | Easy       |                  |          |
|      |                                                  |            |                  |          |
|      |                                                  |            |                  |          |

## Array

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 54   | [Spiral Matrix](https://leetcode-cn.com/problems/spiral-matrix/) | Medium     | 59               |          |
| 59   | [Spiral Matrix II](https://leetcode-cn.com/problems/spiral-matrix-ii/) | Medium     |                  |          |
|      |                                                              |            |                  |          |

## Advanced

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 208  | [Implement Trie Prefix Tree](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) | Medium     |                  |          |
|      |                                                              |            |                  |          |

## DivideAndconquer

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 169  | [Mjority Element](https://leetcode-cn.com/problems/majority-element/) | Easy       |                  |          |
|      |                                                              |            |                  |          |

