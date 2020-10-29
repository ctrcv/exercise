class Solution:
    def translateNum(self, num: int) -> int:
        # 方法1：
        # # https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/435543
        # if num <= 9:
        #     return 1
        #
        # ba = num % 100
        # if ba <= 9 or ba >= 26:
        #     return self.translateNum(num // 10)
        # else:
        #     return self.translateNum(num // 10) + self.translateNum(num // 100)

        # 方法2 & 方法3
        # 方法2通过额外的字符串数组，需要O(N)的空间复杂度，方法三则只需要O(1)的空间复杂度
        # 时间复杂度均为O(N)，即数字的长度
        # https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/solution/mian-shi-ti-46-ba-shu-zi-fan-yi-cheng-zi-fu-chua-6/

        # 方法2：字符串
        # s = str(num)
        # a = b = 1
        # for i in range(2, len(s) + 1):
        #     if '10' <= s[i - 2: i] <= '25':
        #         c = a + b
        #     else:
        #         c = a
        #     b = a
        #     a = c
        #
        # return a

        # 方法3：数字求余，逆序
        a = b = 1
        y = num % 10
        while num:
            num //= 10
            x = num % 10
            a, b = a + b if 10 <= x * 10 + y <= 25 else a, a
            y = x

        return a


N = 1225818
print(Solution().translateNum(N))
