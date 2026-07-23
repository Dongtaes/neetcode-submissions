class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rest = {}

        for (i,num) in enumerate(nums):
            k = target - num
            if k in rest:
                return [rest[k], i]
            rest[num] = i
        
        return [0,0]