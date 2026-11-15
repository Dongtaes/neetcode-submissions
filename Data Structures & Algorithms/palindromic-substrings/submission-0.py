class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            l,r = i,i
            ## odd length:
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
                count +=1
            #even length
            l,r = i, i+1
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                l-=1
                r+=1
                count +=1
        return count

