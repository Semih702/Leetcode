class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashs1=Counter(s1)
        letters=defaultdict(int)
        need=hashs1.total()
        total=0
        started=False
        l=0

        for r,i in enumerate(s2):
            if i in hashs1:
                while l<r and letters[i]==hashs1[i]:
                    if s2[l] in hashs1:
                        letters[s2[l]]-=1
                        total-=1
                        print(total)
                    l+=1
                letters[i]+=1
                total+=1
                if need==total:
                    return True

            else:
                letters=defaultdict(int)
                total=0
                l=r   
        
        return False