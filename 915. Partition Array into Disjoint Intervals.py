# algorithm
"""
iterate the original array three times
(a) first time, record the local max before index i
(b) second time, record the local min after index i
(c) compare (a) and (b) results, id there exists an index i so that the local max of result (a) before index i is less than
    the local min of result (b) after index i + 1, then i + 1 is the answer
"""


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lst1, lst2 = [None for num in nums], [None for num in nums]

        local_max = float('-inf')
        for i in range(n := len(nums)):
            local_max = max(local_max, nums[i])
            lst1[i] = local_max

        local_min = float('inf')
        for i in range(n - 1, -1, -1):
            local_min = min(local_min, nums[i])
            lst2[i] = local_min

        for i in range(n - 1):
            if lst1[i] <= lst2[i + 1]:
                return i + 1