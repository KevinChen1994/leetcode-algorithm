# !usr/bin/env python
# -*- coding:utf-8 _*-
# author:chenmeng
# datetime:2020/9/4 18:08
'''
solution: 使用stack作为辅助，模拟栈的插入和弹出。当栈插入一个元素后，循环判断栈内元素与弹出顺序之间的关系，如果栈顶元素等于弹出顺序第一个元素的话，
那就弹出栈，最终判断stack是否为空，为空说明合法。第二个是一个简写的代码。
'''
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        for item in pushed:
            stack.append(item)
            while stack and popped:
                if stack[-1] == popped[0]:
                    stack.pop()
                    popped.pop(0)
                else:
                    break
        if len(stack) == 0:
            return True
        else:
            return False

    def validateStackSequences(self, pushed, popped):
        stack = []
        for item in pushed:
            stack.append(item)
            while stack and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return not stack


if __name__ == '__main__':
    solution = Solution()
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    # popped = [4, 3, 5, 1, 2]
    print(solution.validateStackSequences(pushed, popped))
