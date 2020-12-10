class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2: return n

        # 滑动窗口思想
        # 方法1： 标记字符的位置
        # dic = {}
        # left, right = 0, 0
        # maxlen = 0
        # while right < n:
        #     c = s[right]
        #
        #     if c in dic:
        #         left = max(dic[c], left)
        #     maxlen = max(maxlen, right - left + 1)
        #     dic[c] = right + 1
        #     right += 1
        #
        # return maxlen

        # 方法2：统计窗口内的字符数
        left, right = 0, 0
        maxlen = 0
        dic = {}
        while right < n:
            if s[right] not in dic:
                dic[s[right]] = 1
                right += 1
                maxlen = max(maxlen, len(dic))
            else:
                del dic[s[left]]
                left += 1

        return maxlen

# S = "abcabcbb"
# S = "bbbbbbbbb"
# S = "pwwkew"
# S = " "
# S = "AU"
# S = "tmmzuxt"
print(len(S))
print(Solution().lengthOfLongestSubstring(S))
