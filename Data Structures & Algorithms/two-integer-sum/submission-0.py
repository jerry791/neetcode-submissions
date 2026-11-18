class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seem={}
        for i in range(len(nums)):
            if target-nums[i] in seem.keys():
                return [seem[target-nums[i]],i]
            else:
                seem[nums[i]]=i