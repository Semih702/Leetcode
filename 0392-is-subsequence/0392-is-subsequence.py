class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        index= 0
        for p in t:
            if p == s[index]:
                index+=1
            if index==len(s):
                break
        
        return index==len(s)
            