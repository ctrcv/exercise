# 代码在某些测试用例出现错误
class Solution:
    def isNumber(self, s: str) -> bool:
        stack = []
        flag = True


        def isOperator(x):
            if x == '+' or x == '-':
                return True

        def isExp(x):
            if x == 'e' or x == 'E':
                return True

        def isPoint(x):
            if x == '.': return True

        if len(s) == 0:
            return False
        if len(s) == 1 and not s.isdigit():
            return False

        for i, c in enumerate(s):
            if i == 0 and (not c.isdigit() or isOperator(c)):
                return False
            if c == ' ':
                continue
            if c.isdigit():
                continue
            elif isOperator(c):
                if i == 0:
                    stack.append(c)
                    continue
                elif len(stack) > 0 and not isExp(stack[-1]):
                    flag = False
                    break
            elif isExp(c):
                if i != len(s) - 1:
                    if len(stack) > 0 and not isOperator(stack[-1]):
                        flag = False
                        break
                    else:
                        stack.append(c)
                else:
                    flag = False
                    break
            elif isPoint(c):
                if len(stack) != 0:
                    if isExp(stack[-1]):
                        flag = False
                        break
                    if isPoint(stack[-1]):
                        flag = False
                        break
                stack.append('.')
            else:
                flag = False
                break

        return flag


s = "1 "
res = Solution().isNumber(s)
print(res)
