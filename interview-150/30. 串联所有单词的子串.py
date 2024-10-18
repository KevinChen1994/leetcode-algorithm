from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        word_total_len = sum([len(word) for word in words])
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        res = []
        # 滑动窗口
        for i in range(len(s) - word_total_len + 1):
            tmp_dict = word_dict.copy()
            for j in range(i, i + word_total_len, len(words[0])):
                word = s[j:j + len(words[0])]
                if word in tmp_dict:
                    tmp_dict[word] -= 1
                    if tmp_dict[word] == 0:
                        del tmp_dict[word]
                else:
                    break
            if not tmp_dict:
                res.append(i)
        return res



if __name__ == '__main__':
    solution = Solution()
    print(solution.findSubstring(s="barfoothefoobarman", words=["foo","bar"]))
        