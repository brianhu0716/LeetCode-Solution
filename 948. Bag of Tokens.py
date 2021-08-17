# algorithm
"""
we can first sort the token array so that when the power is greater than the tokens[i](i is iterate from index 0), we can consume the minimum power to get 1 score
and if our power is less than current token[i], we can consume 1 score to supply the maxima power. The termination will happen when the index i is greater than index j
"""


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = 0
        score, n = 0, len(tokens)
        tokens.sort()
        j = n - 1
        for i in range(n):
            if power >= tokens[i]:
                score += 1
                power -= tokens[i]
            elif score > 0:
                power += tokens[j] - tokens[i]
                j -= 1
            ans = max(ans, score)
            if i > j:
                return ans
        return ans