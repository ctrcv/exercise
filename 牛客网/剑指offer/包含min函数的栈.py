# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        if node is not None:
            self.stack.append(node)
            if len(self.min_stack) > 0:
                if node < self.min_stack[-1]:
                    self.min_stack.append(node)
                else:
                    self.min_stack.append(self.min_stack[-1])
            else:
                self.min_stack.append(node)

    def pop(self):
        # write code here
        if self.stack is not None:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack is not None:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.min_stack is not None:
            return self.min_stack[-1]
