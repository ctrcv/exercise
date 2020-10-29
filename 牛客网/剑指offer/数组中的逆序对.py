# -*- coding:utf-8 -*-

class Solution:
    def InversePairs(self, data):
        # write code here


    def mergerSort(self, arr):
        pass

    def merge(self, arr, suparr, l, r):
        if l + 1 == r:
            if arr[l] <= arr[r]:
                suparr[l], suparr[r] = arr[l], arr[r]
            else:
                suparr[l], suparr[r] = arr[r], arr[l]
            return
        ret = []
        mid = (l + r) // 2
        ret.extend(self.merge(l, mid))
        ret.extend(self.merge(mid+1, r))