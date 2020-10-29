# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n == 0:
            return 0
        left, right = 0, n - 1
        mid = (left + right) // 2
        while left != right - 1:
            if rotateArray[right] < rotateArray[mid]:
                left = mid
            elif rotateArray[left] > rotateArray[mid]:
                right = mid
            mid = (left + right) // 2

        return rotateArray[right]


arr = [4, 5, 6, 7, 8,  1, 2]
print(Solution().minNumberInRotateArray(arr))

