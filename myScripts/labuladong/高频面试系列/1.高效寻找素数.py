"统计一定范围内素数的个数"


# 1.简单法
# def countPrimes(n):
#     nums = 0
#     for i in range(2, n):
#         if isPrime(i):
#             nums += 1
#     return nums
#
# def isPrime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# 2. 高效法, 时间复杂度：O(NloglogN)
def countPrimes(n):
    nums = 0
    isPrime = [True] * n
    i = 2
    while i * i < n:
        if isPrime[i]:
            j = i * i
            while j < n:
                isPrime[j] = False
                j += i
        i += 1

    for i in range(2, n):
        if isPrime[i]:
            nums += 1

    return nums
