class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 改用dict，會變成O(1)
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen: 
                return True
            else:
                seen[nums[i]]=i
        return False