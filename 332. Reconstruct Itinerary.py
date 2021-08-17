class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        for fromi, toi in tickets: # key: from where, value: to where
            d[fromi].append(toi)
        d = {key: sorted(d[key]) for key in d} # for each key, we need to sort the answer will meet the smallest lexical order requirements
        nodes = len(tickets) + 1 # length of the answer

        def dfs(start, path, used): # "start" is the name of start stop, path is the stops we've been visited
            if len(path) == nodes: # visited all stops
                self.ans = path[:]
                return
            if start not in d: # no further stop to move
                return

            for i in range(len(d[start])):
                if i in used[start] or self.ans: # if the index in d[start] has been visited, we pass that situation or we've already find the answer
                    continue
                next_stop = d[start][i] # name of next_stop
                """
                used[start].add(i)
                path.append(next_stop)
                dfs(next_stop, path, used)
                used[start].remove(i)
                path.pop()
                """
                used[start].add(i) # add of the index of next_stop
                dfs(next_stop, path + [next_stop], used)
                used[start].remove(i)

        self.ans = []
        dfs("JFK", ["JFK"], {key: set() for key in d}) # start from "JFK",
        return self.ans