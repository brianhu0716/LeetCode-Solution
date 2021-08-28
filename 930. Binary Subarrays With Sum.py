"""
when the window sum equals to goal, we then consider the situation that whether the right pointer and left pointer can be moved without changing the window sum. For example: nums = [0, 1, 0, 1, 0] & target = 2, when the first time that the window sum == goal, the left and right pointer are at 0 and 3, if we move both right pointer and left pointer one position, it won't chage the window sum because nums[4] = 0 and nums[1] = 0. In this case, for right and left pointer, each of them has two positions can stay and won't affect the goal. so there is 2 * 2 combinations. We use this concept to write algorithm.
Notice that if the goal = 0, the left pointer might be overlap with the right pointer, in this case the total combinations need to be divided by 2, since we can't let the combination with left pointer exceeding the right pointer happen.
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        left, right = 0, 0
        window_sum, ans = 0, 0
        n = len(nums)

        while right < n:
            window_sum += nums[right]
            while left < right and window_sum > goal:
                window_sum -= nums[left]
                left += 1
            if window_sum == goal:
                temp2 = 1
                right += 1
                while right < n and nums[right] != 1:
                    right += 1
                    temp2 += 1

                temp1 = 1
                while left < right and nums[left] != 1:
                    left += 1
                    temp1 += 1
                # print(temp1, temp2)

                if right > left:
                    ans += temp1 * temp2
                else:
                    ans += temp1 * temp2 // 2
            else:
                right += 1
        return ans