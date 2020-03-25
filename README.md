### leetcode-algorithm 

#### 为了提升自己的编码能力和应试能力，用此项目来记录自己刷过的题，并简单记录思路。  
计划先刷热门题目100道，之后根据知识点掌握程度在逐个加强。

|   题号   |  题目类型  |  做题时间  | 备注 |
|  :----: |   :----:  |  :----:   |:----:|
| 01.两数之和  | 数组(easy) | 2019-12-27  ||
| 02.两数相加  | 链表(medium) | 2019-12-28  ||
| 03.无重复字符的最长子串 | 字符串，滑动窗口(medium)|2019-12-30||
|04.寻找两个有序数组的中位数|数组(hard)|2019-12-31||
|05.最长回文子串|字符串，动态规划(medium）|2020-01-14|主要使用的方法就是动态规划，这个问题有利于理解动态规划的思想。另外还有中心拓展算法，Manacher算法(比较复杂，时间为O(N))|
|10.正则表达式匹配|字符串，递归，动态规划(hard)|2020-01-14|重叠子问题，需要使用动态规划去解决|
|11.盛最多水的容器|数组，双指针(medium)|2020-01-15||
|15.三数之和|数组，双指针(medium)|2020-01-15|难度在于如何去重，这里用到的方法就是如果指针的当前值与下一个或者上一个相同，那么跳过|
|17.电话号码的字母组合|字符串，递归(medium)|2020-01-16||
|19.删除链表的倒数第N个节点|链表，双指针(medium)|2020-02-03||
|20.有效的括号|栈(easy)|2020-02-24||
|23.合并K个排序链表|链表，分治算法(hard)|2020-02-26|合并多个链表，先将链表两两合并，然后继续合并|
|31.下一个排列|数组(medium)|2020-02-27|题目描述不太清楚，详解在注释中|
|32.最长有效括号|字符串，动态规划，栈(hard）|2020-02-28|动态规划需要好好看看|
|33.搜索旋转排序数组|数组，二分查找(medium)|2020-02-29||
|34.在排序数组中查找元素的第一个和最后一个位置|数组，二分查找(medium)|2020-02-29|与33题思路一样|
|39.组合总和|数组，回溯算法，深度优先搜索(medium)|2020-03-01|解题思路很有意思|
|42.接雨水|栈，数组，动态规划，双指针(hard)|2020-03-03|多种解题思路|
|46.全排列|回溯算法(medium)|2020-03-04|回溯算法，或者叫做深度优先搜索，与39题思路是一样的|
|49.字母异位词分组|哈希表，字符串(medium)|2020-03-04|熟悉了collections.defaultdict(list)定义字典与ord()函数|
|53.最大子序和|数组，贪心算法，分治算法(easy)|2020-03-05|学习分治算法|
|55.跳跃游戏|数组，贪心算法(medium)|2020-03-08||
|56.合并区间|排序，数组(medium)|2020-03-10||
|62.不同路径|数组，动态规划(medium)|2020-03-10||
|64.最小路径和|数组，动态规划(medium)|2020-03-11||
|70.爬楼梯|动态规划，斐波那契数列(easy)|2020-03-12||
|72.编辑距离|字符串，动态规划(hard)|2020-03-13|状态转移矩阵有点不太好想|
|75.颜色分类|数组，排序，双指针(medium)|2020-03-14||
|76.最小覆盖子串|哈希表，双指针，字符串，滑动窗口(hard)|2020-03-15|滑动窗口的思路还是挺好想出来的，难点在于如何判断滑动窗口内的字符串是否已经全部包含子串的全部字符|
|78.子集|位运算，数组，回溯法(medium)|2020-03-16||
|79.单词搜索|数组，回溯法(medium)|2020-03-16||
|84.柱状图中最大的矩形|数组，栈，分治算法(hard)|2020-03-17|栈的方法不太好想，接雨水那个栈的方法也比较不好想，一起在做一下|
|85.最大矩形|数组，栈，哈希表，动态规划(hard)|2020-03-19|与84题有相同的思路|
|94.二叉树的中序遍历|栈，树，哈希表(medium)|2020-03-21|总结了二叉树遍历的递归法和非递归法的模板|
|96.不同的二叉搜索树|树，动态规划(medium)|2020-03-22|二叉搜索树也是二叉排序树，或者是空树，或者是左节点小于根节点小于右节点|
|98.验证二叉搜索树|树，深度优先搜索(medium)|2020-03-23||
|101.对称二叉树|树，队列，深度优先搜索，广度优先搜索(easy)|2020-03-24|刚知道Python有个库叫Queue，可以通过设置FIFO或者LIFO来实现队列和栈|
|102.二叉树的层次遍历|树，队列，广度优先遍历(medium)|2020-03-25|在collections库中有个deque函数，可以通过append()和popleft()快速实现队列，效率较高。Queue库实现度列的话因为它是为多线程之间安全交换而设计的，所以使用了锁，会导致性能不佳。|