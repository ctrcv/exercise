class MinStack:
    # 方法1.使用辅助栈，辅助栈里存储最小值
    # 当有元素需要入栈的时候，主栈正常压入，辅助栈同时压入该元素和辅助栈栈顶元素中小的元素
    # 元素出栈时，同时推出主栈和辅助栈的栈顶元素
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float("inf")]

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        # 因为主栈与辅助栈的从外界压入的元素树相同，所以当栈中的元素为空时，返回None
        if self.stack:
            return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
