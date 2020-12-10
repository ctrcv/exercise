from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for i, b in enumerate(bills):
            if b == 5:
                five += 1
            elif b == 10:
                if five < 1:
                    return False
                else:
                    five -= 1
                    ten += 1
            else:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True

        # 注释的代码有问题
        # else:
        #     if not changes:
        #         return False
        #     changes.sort(reverse=True)
        #     t = b
        #     for j, c in enumerate(changes):
        #         print("changes: ", changes)
        #         if b == 5:
        #             changes.append(t)
        #             break
        #         elif c <= b:
        #             b -= c
        #             changes.remove(c)
        #         print(j, c, b)

        # return True


# Bills = [5, 5, 5, 10, 20]
# Bills = [5, 5, 5, 10, 10]
# Bills = [10, 10]
# Bills = [5, 5, 10, 10, 20]
Bills = [5, 5, 5, 5, 20, 20, 5, 5, 20, 5]
print(Solution().lemonadeChange(Bills))
