# 题目列表

感谢[花花酱](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) 的分享，将题目按照不同的类别进行分组，并且有难度、相似题目和一些技巧。花花酱在YouTube和B站都有分享解题思路，非常硬核。

## DP

| ID   | name                                                         | Difficulty | Similar Problems                      | Comments                                                     |
| :--- | ------------------------------------------------------------ | ---------- | ------------------------------------- | ------------------------------------------------------------ |
| 730  | [统计不同回文子序列](https://leetcode.cn/problems/count-different-palindromic-subsequences/) | Hard       |                                       |                                                              |
| 978  | [最长湍流子数组](https://leetcode.cn/problems/longest-turbulent-subarray/) | Hard       |                                       |                                                              |
| 70   | [爬楼梯](https://leetcode.cn/problems/climbing-stairs/)      | Easy       | 746、1137                             |                                                              |
| 746  | [使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/) | Easy       |                                       |                                                              |
| 1137 | [第 N 个泰波那契数](https://leetcode.cn/problems/n-th-tribonacci-number/) | Easy       |                                       |                                                              |
| 303  | [区域和检索 - 数组不可变](https://leetcode.cn/problems/range-sum-query-immutable/) | Easy       | 1218                                  |                                                              |
| 1218 | [最长定差子序列](https://leetcode.cn/problems/longest-arithmetic-subsequence-of-given-difference/) | Medium     |                                       |                                                              |
| 53   | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/) | Easy       | 121                                   |                                                              |
| 121  | [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/) | Easy       |                                       |                                                              |
| 62   | [不同路径](https://leetcode.cn/problems/unique-paths/)       | Medium     | 63、64、120、174、931、1210           | 这类题目需要确定好路径是怎么进行的，就是当前位置可以哪些位置到达，依次判断可以到达的路径即可。 |
| 63   | [不同路径 II](https://leetcode.cn/problems/unique-paths-ii/) | Medium     |                                       |                                                              |
| 64   | [最小路径和](https://leetcode.cn/problems/minimum-path-sum/) | Medium     |                                       |                                                              |
| 120  | [三角形最小路径和](https://leetcode.cn/problems/triangle/)   | Medium     |                                       |                                                              |
| 174  | [地下城游戏](https://leetcode.cn/problems/dungeon-game/)     | Hard       |                                       |                                                              |
| 931  | [下降路径最小和](https://leetcode.cn/problems/minimum-falling-path-sum/) | Medium     |                                       |                                                              |
| 1210 | [穿过迷宫的最少移动次数](https://leetcode.cn/problems/minimum-moves-to-reach-target-with-rotations/) |            |                                       |                                                              |
| 85   | [最大矩形](https://leetcode.cn/problems/maximal-rectangle/)  | Hard       | 221、304、1277                        | 定义好dp状态转换，相对容易一些。                             |
| 221  | [最大正方形](https://leetcode.cn/problems/maximal-square/)   | Medium     |                                       |                                                              |
| 304  | [二维区域和检索 - 矩阵不可变](https://leetcode.cn/problems/range-sum-query-2d-immutable/) |            |                                       |                                                              |
| 1277 | [统计全为 1 的正方形子矩阵](https://leetcode.cn/problems/count-square-submatrices-with-all-ones/) | Medium     |                                       |                                                              |
| 198  | [打家劫舍](https://leetcode.cn/problems/house-robber/)       | Medium     | 213、309、740、790、801               |                                                              |
| 213  | [打家劫舍 II](https://leetcode.cn/problems/house-robber-ii/) | Medium     |                                       | 将原数组进行分割，转换成198                                  |
| 309  | [买卖股票的最佳时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium     |                                       |                                                              |
| 740  | [删除并获得点数](https://leetcode.cn/problems/delete-and-earn/) | Medium     |                                       | 转换为打家劫舍                                               |
| 790  | [多米诺和托米诺平铺](https://leetcode.cn/problems/domino-and-tromino-tiling/) | Medium     |                                       |                                                              |
| 801  | [使序列递增的最小交换次数](https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/) | Medium     |                                       |                                                              |
| 279  | [完全平方数](https://leetcode.cn/problems/perfect-squares/)  | Medium     |                                       |                                                              |
| 139  | [单词拆分](https://leetcode.cn/problems/word-break/)         | Medium     | 140、818                              |                                                              |
| 140  | [单词拆分 II](https://leetcode.cn/problems/word-break-ii/)   | Hard       |                                       | 记忆化递归                                                   |
| 818  | [赛车](https://leetcode.cn/problems/race-car/)               | Hard       |                                       |                                                              |
| 300  | [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/) | Medium     | 673、1048                             |                                                              |
| 673  | [最长递增子序列的个数](https://leetcode.cn/problems/number-of-longest-increasing-subsequence/) | Medium     |                                       | 对300的进阶，挺有意思                                        |
| 1048 | [最长字符串链](https://leetcode.cn/problems/longest-string-chain/) | Medium     |                                       |                                                              |
| 96   | [不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/) | Medium     |                                       |                                                              |
| 72   | [编辑距离](https://leetcode.cn/problems/edit-distance/)      | Hard       | 1458、10、44、97、115、712、1187      | 这种都需要分各种情况，一定要分清楚再去写状态转移方程。       |
| 1458 | [两个子序列的最大点积](https://leetcode.cn/problems/max-dot-product-of-two-subsequences/) | Hard       |                                       |                                                              |
| 10   | [正则表达式匹配](https://leetcode.cn/problems/regular-expression-matching/) | Hard       |                                       |                                                              |
| 44   | [通配符匹配](https://leetcode.cn/problems/wildcard-matching/) | Hard       |                                       | 与第10题相比，稍微简单了一点。                               |
| 97   | [交错字符串](https://leetcode.cn/problems/interleaving-string/) | Hard       |                                       | 这类题目不要忘记首先定义好初始状态，有时候不只有dp[[0]][][0]才是True，需要考虑全所有的初始状态，例如：10中的需要判断如果开头是.*的需要将dp矩阵设置到他所代表的位置；97中需要提前定义好s3是s1还是s2谁先来组成的。 |
| 115  | [不同的子序列](https://leetcode.cn/problems/distinct-subsequences/) | Hard       |                                       |                                                              |
| 712  | [两个字符串的最小ASCII删除和](https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/) | Medium     |                                       |                                                              |
| 1187 | [使数组严格递增](https://leetcode.cn/problems/make-array-strictly-increasing/) | Hard       |                                       | 太难了，做了一天！                                           |
| 1143 | [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/) | Medium     |                                       | 很经典的一道题，做过前边几道题，看到这道题就很简单了。       |
| 1092 | [最短公共超序列](https://leetcode.cn/problems/shortest-common-supersequence/) | Hard       |                                       |                                                              |
| 718  | [最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/) | Medium     |                                       |                                                              |
| 1139 | [最大的以 1 为边界的正方形](https://leetcode.cn/problems/largest-1-bordered-square/) | Medium     |                                       |                                                              |
| 688  | [骑士在棋盘上的概率](https://leetcode.cn/problems/knight-probability-in-chessboard/) | Medium     | 576、935                              |                                                              |
| 576  | [出界的路径数](https://leetcode.cn/problems/out-of-boundary-paths/) | Medium     |                                       |                                                              |
| 935  | [骑士拨号器](https://leetcode.cn/problems/knight-dialer/)    | Medium     |                                       |                                                              |
| 322  | [零钱兑换](https://leetcode.cn/problems/coin-change/)        | Medium     | 377、416、494、1043、1220、1262、1269 |                                                              |
| 377  | [组合总和 Ⅳ](https://leetcode.cn/problems/combination-sum-iv/) | Medium     |                                       | 初始状态很重要                                               |
| 416  | [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/) | Medium     |                                       | 322的逆向思维了，难点在于如何转换成01背包问题，实现过程中需要注意每个背包只使用一次，并且需要记住dp状态，不能覆盖之前的正确结果。 |
| 494  | [目标和](https://leetcode.cn/problems/target-sum/)           | Medium     |                                       | 需要转换思想，将其转换为背包问题，说实话挺难想到的           |
| 1043 | [分隔数组以得到最大和](https://leetcode.cn/problems/partition-array-for-maximum-sum/) | Medium     |                                       | 与416问题一样。                                              |
| 1220 | [统计元音字母序列的数目](https://leetcode.cn/problems/count-vowels-permutation/) | Hard       |                                       | 虽然是Hard，但是用背包思想去做还是不难的                     |
| 1262 | [可被三整除的最大和](https://leetcode.cn/problems/greatest-sum-divisible-by-three/) | Medium     |                                       | 背包问题，但是背包重量并不是总和                             |
| 1269 | [停在原地的方案数](https://leetcode.cn/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/) | Hard       |                                       | 整体不难，方向容易搞错                                       |
| 813  | [最大平均值和的分组](https://leetcode.cn/problems/largest-sum-of-averages/) | Medium     | 1278、1335、410                       | 注意分割子数组是按顺序来的                                   |
| 1278 | [分割回文串 III](https://leetcode.cn/problems/palindrome-partitioning-iii/) | Hard       |                                       |                                                              |
| 1335 | [工作计划的最低难度](https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/) | Hard       |                                       |                                                              |
| 410  | [分割数组的最大值](https://leetcode.cn/problems/split-array-largest-sum/) | Hard       |                                       |                                                              |
| 1223 | [掷骰子模拟](https://leetcode.cn/problems/dice-roll-simulation/) | Hard       |                                       | 转移矩阵比较好想，但是如何判断当前数字是否无效，以及他的组合比较困难 |
| 312  | [戳气球](https://leetcode.cn/problems/burst-balloons/)       | Hard       |                                       |                                                              |

## LinkedList

| ID   | name                                                         | Difficulty | Similar Problems | Comments                                                     |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | ------------------------------------------------------------ |
| 2    | [两数相加](https://leetcode.cn/problems/add-two-numbers/)    | Medium     | 445              |                                                              |
| 445  | [两数相加 II](https://leetcode.cn/problems/add-two-numbers-ii/) | Medium     |                  |                                                              |
| 24   | [两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/) | Medium     | 25、206          |                                                              |
| 25   | [K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/) | Hard       |                  |                                                              |
| 206  | [反转链表](https://leetcode.cn/problems/reverse-linked-list/) | Easy       | 92               |                                                              |
| 92   | [反转链表 II](https://leetcode.cn/problems/reverse-linked-list-ii/) | Medium     |                  |                                                              |
| 141  | [环形链表](https://leetcode.cn/problems/linked-list-cycle/)  | Easy       | 142              |                                                              |
| 142  | [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/) | Medium     |                  |                                                              |
| 21   | [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) | Easy       | 23               |                                                              |
| 23   | [合并 K 个升序链表](https://leetcode.cn/problems/merge-k-sorted-lists/) | Hard       |                  | 归并                                                         |
| 160  | [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/) | Easy       |                  | 相同路程，两个人速度相同，即使起点不同，最终也是同时到终点。 |

## HashTable

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 1    | [两数之和](https://leetcode.cn/problems/two-sum/)            | Easy       | 560              |          |
| 560  | [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/) |            |                  |          |

## TwoPointers

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 11   | [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) | Medium     | 42               |          |
| 42   | [接雨水](https://leetcode.cn/problems/trapping-rain-water/)  | Hard       |                  |          |
| 167  | [两数之和 II - 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | Easy       | 15、16           |          |
| 15   | [三数之和](https://leetcode.cn/problems/3sum/)               | Medium     |                  |          |
| 16   | [最接近的三数之和](https://leetcode.cn/problems/3sum-closest/) | Medium     |                  |          |
| 88   | [合并两个有序数组](https://leetcode.cn/problems/merge-sorted-array/) | Easy       |                  |          |

## Tree

| ID   | name                                                         | Difficulty | Similar Problems             | Comments                                    |
| ---- | ------------------------------------------------------------ | ---------- | ---------------------------- | ------------------------------------------- |
| 94   | [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/) | Medium     | 144、145                     | 使用递归和辅助栈两种方法实现                |
| 144  | [二叉树的前序遍历](https://leetcode.cn/problems/binary-tree-preorder-traversal/) | Medium     |                              |                                             |
| 145  | [二叉树的后序遍历](https://leetcode.cn/problems/binary-tree-postorder-traversal/) | Medium     |                              |                                             |
| 100  | [相同的树](https://leetcode.cn/problems/same-tree/)          | Easy       | 101、104、110、111、572、965 |                                             |
| 101  | [对称二叉树](https://leetcode.cn/problems/symmetric-tree/)   | Easy       |                              |                                             |
| 104  | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | Easy       |                              |                                             |
| 110  | [平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/) | Easy       |                              |                                             |
| 111  | [二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) | Easy       |                              |                                             |
| 572  | [另一棵树的子树](https://leetcode.cn/problems/subtree-of-another-tree/) | Easy       |                              |                                             |
| 965  | [单值二叉树](https://leetcode.cn/problems/univalued-binary-tree/) | Easy       |                              |                                             |
| 102  | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | Medium     | 107、103                     |                                             |
| 107  | [二叉树的层序遍历 II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/) | Easy       |                              |                                             |
| 103  | [二叉树的锯齿形层序遍历](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/) | Medium     |                              |                                             |
| 236  | [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium     | 235                          |                                             |
| 235  | [二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Easy       |                              |                                             |
| 199  | [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/) | Medium     |                              | 层次遍历                                    |
| 297  | [二叉树的序列化与反序列化](https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/) | Hard       | 449                          |                                             |
| 449  | [序列化和反序列化二叉搜索树](https://leetcode.cn/problems/serialize-and-deserialize-bst/) | Medium     |                              | 这道题比297有意思，需要考虑二叉搜索树的性质 |
| 508  | [出现次数最多的子树元素和](https://leetcode.cn/problems/most-frequent-subtree-sum/) | Medium     |                              | DFS                                         |
| 124  | [二叉树中的最大路径和](https://leetcode.cn/problems/binary-tree-maximum-path-sum/) | Hard       | 543、687                     |                                             |
| 543  | [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/) | Easy       |                              |                                             |
| 687  | [最长同值路径](https://leetcode.cn/problems/longest-univalue-path/) | Medium     |                              |                                             |
| 105  | [从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium     | 106、889、1008               |                                             |
| 106  | [从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/) | Medium     |                              |                                             |
| 889  | [根据前序和后序遍历构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) | Medium     |                              |                                             |
| 1008 | [前序遍历构造二叉搜索树](https://leetcode.cn/problems/construct-binary-search-tree-from-preorder-traversal/) | Medium     |                              |                                             |

## Graph

| ID   | name                                                         | Difficulty | Similar Problems         | Comments                                             |
| ---- | ------------------------------------------------------------ | ---------- | ------------------------ | ---------------------------------------------------- |
| 133  | [克隆图](https://leetcode.cn/problems/clone-graph/)          | Medium     | 138                      | DFS                                                  |
| 138  | [随机链表的复制](https://leetcode.cn/problems/copy-list-with-random-pointer/) | Medium     |                          |                                                      |
| 200  | [岛屿数量](https://leetcode.cn/problems/number-of-islands/)  | Medium     | 547、695、733、827、1162 | DFS                                                  |
| 547  | [省份数量](https://leetcode.cn/problems/number-of-provinces/) | Medium     |                          | 在美国站中这道题叫朋友圈，只是改了个名字，思路一样。 |
| 695  | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | Medium     |                          |                                                      |
| 733  | [图像渲染](https://leetcode.cn/problems/flood-fill/)         | Easy       |                          |                                                      |
| 827  | [最大人工岛](https://leetcode.cn/problems/making-a-large-island/) | Hard       |                          | 这道题是一道变型题，挺有意思的。                     |
| 1162 | [地图分析](https://leetcode.cn/problems/as-far-from-land-as-possible/) | Medium     |                          | BFS                                                  |

## Search

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 215  | [数组中的第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | Medium     |                  |          |
|      |                                                              |            |                  |          |

## String

| ID   | name                                                    | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------- | ---------- | ---------------- | -------- |
| 415  | [字符串相加](https://leetcode.cn/problems/add-strings/) | Easy       |                  |          |
|      |                                                         |            |                  |          |

## Binary Search

| ID   | name                                              | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------- | ---------- | ---------------- | -------- |
| 69   | [x 的平方根](https://leetcode.cn/problems/sqrtx/) | Easy       |                  |          |
|      |                                                   |            |                  |          |

## Array

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 54   | [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/)      | Medium     | 59               |          |
| 59   | [螺旋矩阵 II](https://leetcode.cn/problems/spiral-matrix-ii/) | Medium     |                  |          |
|      |                                                              |            |                  |          |

## Advanced

| ID   | name                                                         | Difficulty | Similar Problems | Comments |
| ---- | ------------------------------------------------------------ | ---------- | ---------------- | -------- |
| 208  | [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/) | Medium     |                  |          |
|      |                                                              |            |                  |          |

## DivideAndconquer

| ID   | name                                                       | Difficulty | Similar Problems | Comments |
| ---- | ---------------------------------------------------------- | ---------- | ---------------- | -------- |
| 169  | [多数元素](https://leetcode.cn/problems/majority-element/) | Easy       |                  |          |
|      |                                                            |            |                  |          |
