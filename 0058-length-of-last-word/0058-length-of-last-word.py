class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length= 0
        is_space=False
        
        for char in s:
            if char==" ":
                is_space=True
            elif is_space:
                length = 1
                is_space = False
            else:
                length +=1
        return length