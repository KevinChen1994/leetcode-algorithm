from typing import List


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        sid = {s: i for i, s in enumerate(req_skills)}  # 字符串映射到下标
        n = len(people)
        mask = [0] * n
        for i, skills in enumerate(people):
            for s in skills:  # 把 skills 压缩成一个二进制数 mask[i]
                mask[i] |= 1 << sid[s]

        u = 1 << len(req_skills)
        ids = [0] * u  # ids[j] 表示 f[j] 对应的 people 下标集合
        f = [float("inf")] * u  # f[j] 表示并集为 j 至少要选的 people 个数
        f[0] = 0
        for j in range(u - 1):  # f[u-1] 无需计算
            if f[j] == float("inf"): continue  # 无法更新其它状态，直接跳过
            for i, msk in enumerate(mask):
                if f[j] + 1 < f[j | msk]:
                    f[j | msk] = f[j] + 1  # 刷表：用 f[j] 去更新其它状态
                    ids[j | msk] = ids[j] | (1 << i)

        res = ids[-1]
        return [i for i in range(n) if (res >> i) & 1]  # 所有在 res 中的下标





if __name__ == '__main__':
    solution = Solution()
    req_skills = ["java","nodejs","reactjs"]
    people = [["java"],["nodejs"],["nodejs","reactjs"]]
    print(solution.smallestSufficientTeam(req_skills, people))