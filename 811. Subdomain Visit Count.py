class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for cpdomain in cpdomains:
            times, subdomain = cpdomain.split(" ")
            times = int(times)
            subdomain = subdomain.split(".")
            res = subdomain.pop()
            d[res] += times
            for string in subdomain[::-1]:
                res = string + "." + res
                d[res] += times
        ans = []
        for key, val in d.items():
            ans.append(" ".join([str(val), key]))
        return ans