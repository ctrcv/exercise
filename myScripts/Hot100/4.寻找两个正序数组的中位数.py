from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1. 暴力算法
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        return nums1[n // 2] if n % 2 != 0 else (nums1[n // 2 - 1] + nums1[n // 2]) / 2

        # 2.
        # n1, n2 = len(nums1), len(nums2)
        # mid1, mid2 = n1 // 2, n2 // 2
        # tar_idx = (n1 + n2)
        #
        # # nums1[n1], nums2[n2]
        # if n1 < tar_idx:




# Nums1, Nums2 = [1, 3], [2]
# Nums1, Nums2 = [1, 2], [3, 4]
Nums1, Nums2 = [], [3, 4]
print(Solution().findMedianSortedArrays(Nums1, Nums2))
