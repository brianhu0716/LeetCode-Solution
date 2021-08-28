class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i in range(n := len(nums)):
            if i in visited: # visited this index
                continue
            path = set()
            while True:
                if i in path:
                    return True
                path.add(i)
                visited.add(i)
                prev, i = i, (i + nums[i]) % n # find the next index and save the current index as previous index
                if prev == i or nums[i] * nums[prev] < 0: # make sure the circular loop definition is not been violated
                    break
        return False