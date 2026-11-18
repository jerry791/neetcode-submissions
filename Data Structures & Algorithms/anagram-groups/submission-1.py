from collections import Counter, defaultdict, deque
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return[[""]]
        if len(strs)<1:
            return [strs]
        seem=defaultdict(list)
        for i in range(len(strs)):
            tmp=str(sorted(Counter(strs[i]).items())) #指紋
            seem[tmp].append(strs[i])
        return list(seem.values())
        