from collections import deque, defaultdict, Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seem=dict(Counter(nums))
        sorted_seem=dict(sorted(seem.items(), key=lambda item: item[1],reverse=True))
        return list(sorted_seem.keys())[:k]