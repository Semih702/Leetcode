class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length= 0
        is_space=False
        
        for char in s[::-1]:   
            if char!=" ":
                length+=1
            elif length>0:
                return length

        return length