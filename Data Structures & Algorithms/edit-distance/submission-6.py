class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #  m o
        # m0 0
        # o0 0
        n = len(word2) + 1
        m = len(word1) +1
        dp = [[0] * (m) for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    continue
                # matches?
                add = 1 
                if i<n-1 and j<m-1 and word2[i] == word1[j]:
                    add = 0
                
                res1, res2, res3 = n + m, n + m, n + m

                if i+1<n:
                    res1 = dp[i+1][j] +1 
                if j+1<m:
                    res2 = dp[i][j+1] +1
                if j+1<m and i+1<n:
                    res3 = dp[i+1][j+1] + add
                dp[i][j] = min(res1, res2, res3)
        
        return dp[0][0]
                

                



