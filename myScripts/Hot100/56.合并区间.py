from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 方法：排序 & 合并。时间和空间复杂度取决于排序的复杂度，即O(NlogN)，空间O(logN)，
        # 对每个区间的左端点进行排序
        intervals.sort(key=lambda x: x[0])

        merged = []
        for int in intervals:
            # 如果列表为空，或当前区间与上一个区间不重合，则直接添加
            if not merged or merged[-1][1] < int[0]:
                merged.append(int)
            else:
                # 否则，可以对区间进行合并
                merged[-1][1] = max(merged[-1][1], int[1])
        return merged



