# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        n = len(sequence)
        root = sequence[-1]
        i = 0
        while i < n:
            if sequence[i] < root:
                i += 1
            else:
                break

        j = i
        while j < n - 1:
            if sequence[j] > root:
                j += 1
            else:
                return False

        left = right = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if i < n - 1:
            right = self.VerifySquenceOfBST(sequence[i: j])

        return left and right

