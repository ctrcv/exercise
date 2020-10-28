from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        countMap = {}
        for num in arr:
            countMap[num] = countMap.get(num, 0) + 1

        # countArr = [0] * (len(arr) + 1)
        # for k, v in countMap.items():
        #     if countArr[v] > 0:
        #         return False
        #     else:
        #         countArr[v] += 1
        #
        # return True
        countSet = set()
        for k, v in countMap.items():
            if v in countSet:
                return False
            else:
                countSet.add(v)
        return True


# Arr = [1, 2, 2, 1, 1, 3]
Arr = [1, 2]
print(Solution().uniqueOccurrences(Arr))
