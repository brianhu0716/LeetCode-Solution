"""
always make sure that for any index i, nums[i - 1] < nums[i] > nums[i - 1] will hold
if len(nums) is even, example: [0, 1, 2, 3, 4, 5] -- > [0, 4, 2, 3, 1, 5] ([low, high, low, high, low, high])
if len(nums) is odd, example: [0, 1, 2, 3, 4] --> [0, 4, 2, 3, 1] ([low, high, low, high, low])
we just need to set the different start index of j and keep stride of i and j as 2. the algorithm can easily be implemented.
"""


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        if n % 2 == 0:
            i, j = 1, len(nums) - 2
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j -= 2
        else:
            i, j = 1, len(nums) - 1
            while i <= j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j -= 2
        return nums