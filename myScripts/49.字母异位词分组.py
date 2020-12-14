from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        # 方法1. 字符串排序,时间复杂度O(nklog(k))，k是字符串的最大长度， 空间复杂度O（nk）
        # dic = {}
        # for s in strs:
        #     # 对字符串进行排序，异位词排序后的字符串相同
        #     key = "".join(sorted(s))
        #     if key not in dic:
        #         dic[key] = [s]
        #     else:
        #         dic[key].append(s)
        #
        # return list(dic.values())

        # 方法2：计数,时间复杂度O（n（k+26）），生成哈希表的键需要O（26）的时间复杂度
        dic = {}
        for s in strs:
            # 两个字符串中的相同字母出现的次数一定是相同的
            # 故可以将每个字母出现的次数使用字符串表示
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            # 数组需要转换成tuple才能哈希
            key = tuple(count)
            if key not in dic:
                dic[key] = [s]
            else:
                dic[key].append(s)

        return list(dic.values())


Strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(Strs))
