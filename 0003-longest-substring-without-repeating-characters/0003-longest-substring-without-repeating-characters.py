class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp=0
        maks=0
        aset=set()
        for rp in range(len(s)):
            while s[rp] in aset:
                aset.remove(s[lp])
                lp+=1
            aset.add(s[rp])
            maks=max(rp-lp+1,maks)
        return maks
    
