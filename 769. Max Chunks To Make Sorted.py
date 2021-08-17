# algorithm
"""
three conditions need to be concerned
(a) if the current value(target) is less than previous min value, it means we need to merge this value to previous sud-list continuously until one of the following condition is met
    (1) if we meet a local_max[j] is less than target, we need to merge the index j + 1: sub-list to one sub-list and set the local min of it as target and the local max is the
        max value between local_max[j + 1: ]
    (2) if local min[j] < target < local_max, we know the target need to be merged into the sub-list with index = j, and the sub-list form j: end need to merge as one sub-list and
        again we need to reset the local max value with index = j
    (3) if the target is greater than local max with index = -1, it means we can create another sub-list to maximize the number of the sub-list to meet the requirements
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def trackBack(target, local_min, local_max):
            for j in range(len(local_min) - 1, -1, -1):
                if target > local_max[j]:
                    local_min[j + 1] = target
                    local_max[j + 1] = max(local_max[j + 1:])
                    return local_min[: j + 2], local_max[: j + 2]
                if local_min[j] < target < local_max[j]:
                    local_max[j] = max(local_max[j:])
                    return local_min[: j + 1], local_max[: j + 1]
            return [target], [max(local_max)]

        local_min, local_max = [arr[0]], [arr[0]]
        for i in range(1, len(arr)):
            # print(arr[i], local_min, local_max)
            if arr[i] <= local_min[-1]:
                local_min, local_max = trackBack(arr[i], local_min, local_max)
            elif local_min[-1] < arr[i] < local_max[-1]:
                continue
            else:
                local_min.append(arr[i])
                local_max.append(arr[i])

        return len(local_max)