class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 0:
            return -1

        digits = 1
        while True:
            number = self.countOfInt(digits)
            if n < number * digits:
                return self.digitAtIndex(n, digits)
            n -= digits * number
            digits += 1

    def digitAtIndex(self, index, digits):
        # index位置对应的数字
        number = self.beginNumber(digits) + index // digits  # index对应的digits位数的整数
        indexFromRight = digits - index % digits
        for i in range(1, indexFromRight):
            number /= 10

        return int(number % 10)

    def beginNumber(self, digits):
        # 该区间的初始数字
        if digits == 1:
            return 0
        return int(pow(10, digits - 1))

    def countOfInt(self, digits):
        # 计算位数digits包含的数字数量
        # 如2位数：10-99共90个数; 3位数：100-999共900个数
        if digits == 1:
            return 10

        cnt = int(pow(10, digits - 1))
        return 9 * cnt


print(Solution().findNthDigit(19))