class Solution:
    def climbStairs(self, n: int) -> int:
        dp1, dp2 = 1,1

        for i in range(n-2, -1, -1):
            tmp = dp1
            dp1 = dp1 + dp2
            dp2 = tmp

        return dp1