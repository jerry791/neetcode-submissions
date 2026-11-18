from collections import Counter, defaultdict, deque
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seem=defaultdict(list)
        for i in strs:
            tmp= "".join(sorted(i))
            seem[tmp].append(i)
        return list(seem.values())
        