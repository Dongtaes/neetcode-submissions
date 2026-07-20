class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1 
        while l < r:
            while l<=r and  str(s[l]).isalnum() is False :
                l+=1
            while r>=l and  str(s[r]).isalnum() is False:
                r-=1
            if r<=l:
                return True
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
            
        return True