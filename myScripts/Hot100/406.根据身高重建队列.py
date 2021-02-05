from typing import List


# 排序,for循环,需要额外的O(n)的res空间
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # （套路）：一般这种数对，还涉及排序的，根据第一个元素正向排序，根据第二个元素反向排序;
        # 或者根据第一个元素反向排序，根据第二个元素正向排序，往往能够简化解题过程。
        if not people: return people
        # 首先对数对进行排序,按照数对元素1进行降序,数对元素2进行升序
        # 原因是按照元素1进行降序排序,对于每个元素,在其之前的元素的个数,就是大于等于他的元素的数量
        # 按照第二个元素进行升序排序,是因为希望k大的尽量在后面,减少插入操作的次数,也是为了保证正确性
        people.sort(key=lambda x: (-x[0], x[1]))
        # 下面排序的结果不符合后面的res生成代码逻辑
        # people.sort(key=lambda x: (-x[0]))
        # people.sort(key=lambda x: x[1])

        res = []
        for p in people:
            # p[1]大于res的长度,说明p的位置应该处于后面
            if len(res) <= p[1]:
                res.append(p)
            # 否则,将元素插入到p[1]值对应的索引处
            else:
                res.insert(p[1], p)

        return res

# # 排序,while循环,不需要额外的空间
# class Solution:
#     def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
#         people.sort(key=lambda x: (-x[0], x[1]))
#         i = 0
#         while i < len(people):
#             if i > people[i][1]:
#                 people.insert(people[i][1], people[i])
#                 people.pop(i + 1)
#             i += 1
#
#         return people


People = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
print(Solution().reconstructQueue(people=People))
