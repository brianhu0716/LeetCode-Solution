class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sum = [0]
        min_len = float('inf')
        n = len(arr)
        dp = [float('inf') for i in range(n + 1)]
        left = 0

        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + arr[i])
            if prefix_sum[-1] < target:
                continue

            right = i + 1
            while left <= right:
                mid = (left + right) // 2
                if prefix_sum[-1] - prefix_sum[mid] < target:
                    right = mid - 1
                elif prefix_sum[-1] - prefix_sum[mid] > target:
                    left = mid + 1
                else:
                    break

            if prefix_sum[-1] - prefix_sum[mid] == target: # sub-array with sun equals to target
                len_now = i + 1 - mid # calculate the length
                len_prev = dp[mid] # min length of previous sub-array with sum equals to target
                dp[i + 1] = min(dp[i], len_now) # set dp[i] as the min length of the sub-array with sum equals to target
                min_len = min(min_len, len_now + len_prev)
            else:
                dp[i + 1] = dp[i] # if the sub-array doesn't equal to target, dp[i] inherits the dp[i - 1] answer

        return min_len if min_len != float('inf') else -1