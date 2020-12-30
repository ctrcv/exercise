from typing import List


# 1.二分查找法，时间复杂度O(n!)，空间复杂度O(1)
# class Solution:
#     def binary_search(self, matrix, target, start, vertical):
#         lo = start
#         hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1
#
#         while hi >= lo:
#             mid = (lo + hi) // 2
#             if vertical:  # searching a column
#                 if matrix[start][mid] < target:
#                     lo = mid + 1
#                 elif matrix[start][mid] > target:
#                     hi = mid - 1
#                 else:
#                     return True
#             else:  # searching a row
#                 if matrix[mid][start] < target:
#                     lo = mid + 1
#                 elif matrix[mid][start] > target:
#                     hi = mid - 1
#                 else:
#                     return True
#
#         return False
#
#     def searchMatrix(self, matrix, target):
#         # an empty matrix obviously does not contain `target`
#         if not matrix:
#             return False
#
#         # iterate over matrix diagonals starting in bottom left.
#         for i in range(min(len(matrix), len(matrix[0]))):
#             vertical_found = self.binary_search(matrix, target, i, True)
#             horizontal_found = self.binary_search(matrix, target, i, False)
#             if vertical_found or horizontal_found:
#                 return True
#
#         return False

# 2.从左下角开始搜索，当目标值比当前位置的值大，指针右移，否则左移
# 时间复杂度：O(m + n), 空间O(1)
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False
