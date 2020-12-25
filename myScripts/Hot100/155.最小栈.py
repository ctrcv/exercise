# class MinStack:
#     # 方法1.使用辅助栈，辅助栈里存储最小值
#     # 当有元素需要入栈的时候，主栈正常压入，辅助栈同时压入该元素和辅助栈栈顶元素中小的元素
#     # 元素出栈时，同时推出主栈和辅助栈的栈顶元素
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min_stack = [float("inf")]
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#         self.min_stack.append(min(x, self.min_stack[-1]))
#
#     def pop(self) -> None:
#         self.stack.pop()
#         self.min_stack.pop()
#
#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1]
#
#     def getMin(self) -> int:
#         # 因为主栈与辅助栈的从外界压入的元素树相同，所以当栈中的元素为空时，返回None
#         if self.stack:
#             return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 栈中保存差值。时间复杂度O(1), 空间复杂度O(1)
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = -1

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min_value = x
        else:
            diff = x-self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self) -> None:
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self) -> int:
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self) -> int:
        return self.min_value if self.stack else -1