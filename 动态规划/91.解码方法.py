class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        pre, curr = 1, 1
        for i in range(1, n):
            tmp = curr
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    curr = pre
                else:
                    return 0
            elif s[i - 1] == '1' or (s[i - 1] == '2' and '1' <= s[i] <= '6'):
                curr += pre
            pre = tmp
        return curr

# S = "226"
# S = "10"
# S = "2101"
S = "1201234"
print(Solution().numDecodings(S))
