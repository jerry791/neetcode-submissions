from collections import Counter, defaultdict, deque
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return[[""]]
        if len(strs)<1:
            return [strs]
        # test='test'
        # test2='estt'
        # print(str(Counter(test).most_common()))
        # print(str(Counter(test2).most_common()))
        seem=defaultdict(list)
        for i in range(len(strs)):
            tmp=str(sorted(Counter(strs[i]).items())) #指紋
            seem[tmp].append(strs[i])
        return list(seem.values())
        