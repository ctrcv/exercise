#
# retrun the longest increasing subsequence
# @param arr int整型一维数组 the array
# @return int整型一维数组
#
class Solution:
    def LIS(self, arr):
        # write code here
        # 第一步：利用贪心+二分求最长递增子序列长度
        res = []
        maxLen = []
        if not arr:
            return res
        res.append(arr[0])
        maxLen.append(1)

        for i in range(1, len(arr)):
            if arr[i] > res[-1]:
                res.append(arr[i])
                maxLen.append(len(res))
            else:
                pos = self.lower_bound(res, arr[i])
                res[pos] = arr[i]
                maxLen.append(pos + 1)

        # 第二步：填充最长递增子序列
        j, k = len(arr) - 1, len(res)
        while k > 0:
            if maxLen[j] == k:
                k -= 1
                res[k] = arr[j]

            j -= 1

        return res

    def lower_bound(self, arr, val):
        # 返回有序数组arr中第一个比val大的值的索引
        for i, a in enumerate(arr):
            if a >= val:
                return i
        return -1


nums = [1, 2, 8, 3, 0, 4]
r = Solution().LIS(nums)
print(r)
