class Solution:
    def isValid(self, s: str) -> bool:
        checkMap = {'{': '}','[': ']', '(': ')'}
        stack = []
        for c in s:
            if c in checkMap.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != checkMap[stack.pop()] :
                    return False
        
        return True if len(stack) == 0 else False