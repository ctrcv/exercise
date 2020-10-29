def LRU(operators, k):
    memo = dict()
    global p
    p = 0

    def set(key, val):
        global p
        p += 1
        memo[key] = [val, p]

    def get(key):
        if key not in memo:
            return -1

        val = memo[key][0]
        # del memo[key]

        global p
        p = get_maxp()
        t = p
        x = memo[key][1]
        update_p(x)
        memo[key][1] = t

        return val

    def get_maxp():
        tmp = -1
        for k, v in memo.items():
            if v[1] > tmp:
                tmp = v[1]
        return tmp

    def del_back():
        key = None
        tmp = float('INF')
        for k, v in memo.items():
            if v[1] < tmp:
                tmp = v[1]
                key = k
        del memo[key]

        update_p()

    def update_p(x=None):
        tmp = -1
        for k, v in memo.items():
            if v[1] > 0:
                if x:
                    if v[1] > x:
                        v[1] -= 1
                else:
                    v[1] -= 1
            if v[1] > tmp:
                tmp = v[1]
        global p
        p = tmp

    for opt in operators:
        print(memo)
        if len(opt) == 3 and opt[0] == 1:
            set(opt[1], opt[2])
            if len(memo) > k:
                del_back()
        elif len(opt) == 2 and opt[0] == 2:
            val = get(opt[1])
            print([opt[1], val])


opts, m = [[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3
LRU(opts, m)


#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
# import collections
# class Solution:
#     def __init__(self, k):
#         self.dic = collections.OrderedDict()
#         self.capacity = k
#
#     def get(self, key):
#         if key not in self.dic: return -1
#         val = self.dic.pop(key)
#         self.dic[key] = val
#         return val
#
#     def set(self, key, value):
#         if key in self.dic:
#             self.dic.pop(key)
#         else:
#             if self.capacity > 0:
#                 self.capacity -= 1
#             else:
#                 self.dic.popitem(last=False)
#         self.dic[key] = value
#
# s = input().strip()
# idx = s.index("]],")
# k = int(s[idx+3:])
# ss = s[:idx]
# aa = ss.strip("[[").split("],[")
# s = Solution(k)
# res = []
# for r in aa:
#     ss = list(map(int, r.strip().split(",")))
#     if ss[0] == 1:
#         s.set(ss[1], ss[2])
#     elif ss[0] == 2:
#         x = s.get(ss[1])
#         res.append(x)
# print(s.dic)
# print(str(res).replace(" ", ""))