class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1, dp2 = 0, 0

        for i in range(len(nums)):
            tmp = dp2
            dp2 = max(dp1+nums[i], dp2)
            dp1 = tmp
        return dp2
