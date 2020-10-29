if __name__ == '__main__':
    N = int(input())
    a = [int(i) for i in input().strip().split()]
    Q = int(input())
    ss = 0
    for _ in range(Q):
        l, r = map(int, input().strip().split())
        for j in range(l, r + 1):
            ss += a[j]
    ss %= 1000000007
    print(ss)
