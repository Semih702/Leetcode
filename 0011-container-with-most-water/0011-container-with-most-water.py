class Solution:
    def maxArea(self, height: List[int]) -> int:
        amount=0
        lp=0
        rp=len(height)-1
        while rp>lp:
            amount=max(amount,((rp-lp)*min(height[lp],height[rp])))
            if(height[lp]>height[rp]):
                rp-=1
            else:
                lp+=1

        return amount
            
                