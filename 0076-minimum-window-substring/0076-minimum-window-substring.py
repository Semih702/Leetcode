

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not t: return ""
        
        letters=Counter(t)
        state=defaultdict(int)
        l=0
        resleft,resright=0,float("inf")

        totalneed=letters.total()
        totalnow=0
        
        for r,ch in enumerate(s):
            if ch in letters:
                state[ch]+=1
                if state[ch]<=letters[ch]:
                    totalnow+=1
            while totalnow==totalneed:
                if resright-resleft > r-l:
                    resleft,resright=l,r
                if s[l] in state:
                    state[s[l]]-=1
                    if state[s[l]]<letters[s[l]]:
                        totalnow-=1
                l+=1


        return s[resleft:resright+1] if resright!=float("inf") else ""