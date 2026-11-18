class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        basket=[]
        for i in nums:
            if i in basket:
                return True
            else: 
                basket.append(i)
        return False