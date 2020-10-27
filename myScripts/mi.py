"""
现在有一幅扑克牌，去掉大小王52张牌。随机选出4张牌，可以任意改变扑克牌的顺序，
并填入 + - * / 四个运算符，不用考虑括号，除法按整数操作，计算过程中没有浮点数，问是否能够求值得到给定的数m。

输入描述: 一行四个数字 （JQK 分别被替换成11，12，13）单空格分割，另一行输入 m
输出描述: 可以输出1, 否则输出0
"""


def fun(nums, m):
    def dfs(exp, s, i):
        if i == 4:
            if str(s) == m:
                # print(exp[:-1])
                return True
            return False

        exp = exp + str(nums[i])
        s = eval(exp)

        return dfs(exp + '+', s, i + 1) or dfs(exp + '-', s, i + 1) \
               or dfs(exp + '*', s, i + 1) or dfs(exp + '//', s, i + 1)

    return dfs('', 0, 0)


if __name__ == '__main__':
    numbers = input().strip().split()
    tar = input().strip()
    res = '1' if fun(numbers, tar) else '0'
    print(res)
