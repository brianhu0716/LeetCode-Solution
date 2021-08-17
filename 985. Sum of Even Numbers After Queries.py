# algorithm
"""
we first calculate the evenSum and oddSum in original array, then we consider two condition
for idx, val in queries
(a) if nums[idx] is even:
    (1) if nums[idx] + val is even, we can change evenSum directly and the oddSum will not be affected
    (2) if nums[idx] + val is odd, we need to substrate nums[idx] from evenSum and add nums[idx] + val to oddSum
(b) if nums[idx] is odd:
    (1) if nums[idx] + val is even, we need to substrate nums[idx] from oddSum and add nums[idx] + val to evenSum
    (2) if nums[idx] + val is odd, we can change oddSum directly and the evenSum will not be affected

last we need to assign nums[idx] + val to nums[idx], and append the evenSum of current state
"""


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum, oddSum = 0, 0
        for num in nums:
            if num % 2 == 0:
                evenSum += num
            else:
                oddSum += num
        arr = list()
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                if (nums[idx] + val) % 2 == 0:
                    evenSum += val
                else:
                    oddSum += (nums[idx] + val)
                    evenSum -= nums[idx]
            else:
                if (nums[idx] + val) % 2 == 0:
                    oddSum -= nums[idx]
                    evenSum += (nums[idx] + val)
                else:
                    oddSum += val
            nums[idx] += val
            arr.append(evenSum)
        return arr