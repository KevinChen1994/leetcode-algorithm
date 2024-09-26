from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0
    
        for word in words:
            # 当前行加上下一个单词后的总字符数是否超过最大宽度
            if num_of_letters + len(word) + len(cur) > maxWidth:
                # 处理当前行
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '  # 分配空格
                res.append(''.join(cur))
                cur, num_of_letters = [], 0  # 重置
            cur.append(word)
            num_of_letters += len(word)
        
        # 处理最后一行：左对齐
        res.append(' '.join(cur).ljust(maxWidth))
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))