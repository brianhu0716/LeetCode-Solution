# algorithm
"""
to meet start j > end i for i <= j and start j is minimized, our first job is to sort the array and record the original position of each interval. Then we consider three possibilities
(a) if intervals[i][1] > intervals[i][0]:
    for this case, the right interval is itself
(b) if intervals[i + 1][0] > intervals[i][1]
    for this case, the right interval index of intervals[i] is original index of intervals[i + 1]
(c) the final case is when the right intervals of intervals[i] is in the very back position or even doesn't exist(intervals[i][1] is too large):
    for this case, we need to store the intervals[i] in a stack(monotonic increasing), we can use binary search to optimize the process to find
    the appropriate position to insert
for each new iteration, we always check the start value of current interval and compare it to the end value of the most left intervals in stack,
if greater, it means we find the right interval of the interval at the most left position in stack, we just popleft it and continue the process

Notice: since the answer array is initialized to be a -1 1-D array, if the iteration is over and there are still some intervals in stack, we just ignore them because
all of them don't have right intervals and its original index in answer need to be assign to -1 which we've already done at the very begin
"""


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals = [(start, end, index) for index, (start, end) in enumerate(intervals)]
        intervals.sort(key=lambda x: x[0])
        stack = deque([])
        ans = [-1 for _ in intervals]

        for i in range(n := len(intervals)):
            while stack and stack[0][1] <= intervals[i][0]:
                _, _, idx = stack.popleft()
                ans[idx] = intervals[i][2]
            if i == n - 1:
                return ans

            if intervals[i][0] == intervals[i][1]:
                ans[intervals[i][2]] = intervals[i][2]
                continue

            if intervals[i][1] > intervals[i + 1][0]:
                j, k = 0, len(stack) - 1
                target = intervals[i][1]
                while j <= k:
                    mid = (j + k) // 2
                    if stack[mid][1] > target:
                        k = mid - 1
                    else:
                        j = mid + 1
                stack.insert(j, intervals[i])
            else:
                ans[intervals[i][2]] = intervals[i + 1][2]