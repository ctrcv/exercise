class Solution:
    def decoder(self, ss):
        if not ss:
            return
        stack = []
        s = ss[::-1]
        for c in s:
            if c != '%':
                stack.append(c)
            else:
                stack = self._decoder(stack)

        return ''.join(stack[::-1])

    def _decoder(self, stack):
        c1 = stack.pop()
        c2 = stack.pop()
        t = chr(int(c1 + c2, 16))
        if t == '%':
            stack = self._decoder(stack)
        else:
            stack.append(t)
        return stack


def main():
    N = int(input())
    for i in range(N):
        S = input()
        print(Solution().decoder(S))


if __name__ == '__main__':
    main()

# S = 'c%%%3%3325%325%3%32d%31%2%25%3%%%3333%35%32E%3%2%3533%2%%36%36%2B%%%332%%325%36%31%6%%332%3%3%2532a'
# print(Solution().decoder(S))
