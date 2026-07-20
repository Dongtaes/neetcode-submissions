class Solution:


    def combinationSum(self, nums, target):
        # dp[i] will store all unique combinations that sum to i
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]] # Base case: one way to make 0 is an empty list

        for num in nums:
            for i in range(num, target + 1):
                for combo in dp[i - num]:
                    # We create a NEW list [num] + combo to avoid 
                    # mutating existing lists in the DP table
                    dp[i].append(combo + [num])
        
        return dp[target]