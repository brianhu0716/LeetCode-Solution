# algorithm
"""
special case: if there exists any letter in b but not exists in a, we just return -1(impossible)
two possibilities need to be concerned
(a) if length a > length b:
    for this case, if b in a, return 1(no need to repeat), if b in a + a, return 2(b is consist of part of tail a and part of head a)
(b) if length b < length a:
    for this case, we need to find where the b exactly equal to a, and check the previous string is the tail of a(if not, return -1).
    Then we just count the repeat time of a in b until we meet a sub-string that disqualified the b[j: j + la] == a condition.
    Finally, if the tail of b exactly equals to a, we can return the count number of repeat time of a, else we need to check if the
    remaining sub-string is the match the head of a, if so, we can return count + 1 else -1
"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if len(set(b) - set(a)) > 0:
            return -1

        if b in a:
            return 1

        if b in a + a:
            return 2

        la, lb = len(a), len(b)
        for i in range(lb):
            if a != b[i: i + la]:
                continue

            if b[: i] != a[-len(b[: i]):] and i != 0:
                return -1

            ans = 1 if i != 0 else 0
            for j in range(i, lb, la):
                if b[j: j + la] != a:
                    break
                ans += 1
            if j + la == lb:
                return ans
            if b[j:] != a[: len(b[j:])]:
                return -1
            return ans + 1
        return -1