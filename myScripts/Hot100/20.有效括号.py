class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == "[" or c == "{":
                stack.append(c)
            elif not stack or self._getRightParent(c) != stack.pop():
                return False

        return not stack
        #     elif c == ")" and (not stack or stack.pop() != "(") :
        #         return False
        #     elif c == "]" and (not stack or stack.pop() != "["):
        #         return False
        #     elif c == "}" and (not stack or stack.pop() != "{"):
        #         return False
        #
        # return True if not stack else False

    def _getRightParent(self, ch):
        if ch == ")": return "("
        if ch == "]": return "["
        if ch == "}": return "{"


# S = "()[]{()}"
S = "]"
print(Solution().isValid(S))
