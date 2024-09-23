

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        result = [""] * numRows
        direction = -1
        cur_row = 0 # 当前行
        for char in s:
            result[cur_row] += char
            # 如果达到最上或者最下，改变方向
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            cur_row += direction
        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s = "PAYPALISHIRING", numRows = 3))