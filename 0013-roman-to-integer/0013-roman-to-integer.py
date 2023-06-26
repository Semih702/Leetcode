class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        value=0
        lastvalue=0
        for i in s:
            if roman[i]>lastvalue:
                value+=roman[i]-lastvalue*2
            else:
                value+=roman[i]
            lastvalue=roman[i]    
        return value 
