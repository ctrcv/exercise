# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        ss = [[0, -1]] * (ord('z') - ord('a') + 1)
        a = ord('a')
        for idx, e in enumerate(s):
            asic = ord(e) - a
            print(asic)
            ss[asic][0] += 1
            ss[asic][1] = idx
            print(ss)

        print(ss)
        for i, c in enumerate(ss):
            if c == 1:
                return s.find(chr(i + a))

        return -1


# S = "abaccdeff"
S = "google"
print(Solution().FirstNotRepeatingChar(S))
