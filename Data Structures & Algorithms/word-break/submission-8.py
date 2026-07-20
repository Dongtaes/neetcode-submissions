class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True
        print(wordDict)
        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                if not ((len(word)+ i) <= len(s) ):
                    continue
                # if the word matches
                if word == s[i:i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break 
        return dp[0]