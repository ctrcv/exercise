class Solution():
    def judgeCircle(self, moves):

        x, y = 0, 0
        for m in moves:
            if m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
            elif m == 'L':
                x -= 1
            elif m == 'R':
                x += 1

        return x == y == 0
        # if not x and not y:
        #     return True
        # else:
        #     return False


action = 'LLDDRUUR'
s = Solution().judgeCircle(action)
print(s)
