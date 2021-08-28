"""
to guarantee that no two adjacent elements share the same value, we just need to sort the array by the frequency of every element, and we put the most frequent values in the
even index until the total length is reached, then we filled odd index from most frequent elements to least frequent elements
"""

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        d, n = defaultdict(int), len(barcodes)
        for num in barcodes:
            d[num] += 1
        pairs = sorted([[key, val] for key, val in d.items()], key=lambda x: x[1])
        ans = [None] * n
        for i in range(0, n, 2):
            ans[i] = pairs[-1][0]
            pairs[-1][1] -= 1
            if pairs[-1][1] == 0:
                pairs.pop()
        for i in range(1, n, 2):
            ans[i] = pairs[-1][0]
            pairs[-1][1] -= 1
            if pairs[-1][1] == 0:
                pairs.pop()
        return ans