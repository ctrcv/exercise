
class Solution(object):
    def findMinLength(self, arr, subarr):
        if not arr or not subarr:
            return 0
        minlen = 1000001
        left, right = 0, 0
        match = 0
        windows = dict()
        needs = dict()
        for n in subarr:
            needs[n] = needs.get(n, 0) + 1

        while right < len(arr):
            c = arr[right]
            if c in needs:
                windows[c] = windows.get(c, 0) + 1
                if windows[c] == needs[c]:
                    match += 1

            while match == len(needs):
                minlen = min(minlen, right - left + 1)
                c2 = arr[left]
                if c2 in needs:
                    windows[c2] -= 1
                    if windows[c2] < needs[c2]:
                        match -= 1
                left += 1

            right += 1

        return minlen if minlen != 1000001 else 0


# Arr = [4, 2, 1, 3]
# sub = [2, 3]
# print(Solution().findMinLength(Arr, sub))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        # print(Solution().findSubArrayLength(Arr, SubArr))
        Arr = list(map(int, input().strip().split()))
        M = int(input())
        SubArr = list(map(int, input().strip().split()))
        print(Solution().findMinLength(Arr, SubArr))
