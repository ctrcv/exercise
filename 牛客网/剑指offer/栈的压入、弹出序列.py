# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) != len(popV):
            return False

        n = len(pushV)
        stack = []
        i = j = 0
        while i < n:
            if pushV[i] != popV[j]:
                stack.append(pushV[i])
                i += 1
            else:
                i += 1
                j += 1

                while stack and stack[-1] == popV[j]:
                    j += 1
                    stack.pop()
        return len(stack) == 0
