class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]: 
        
        res=[]
        non_increasing=deque()
                
        l,r=0,0

        for r in range(len(nums)):
            while non_increasing and nums[non_increasing[-1]]<nums[r]:
                non_increasing.pop()
            
            non_increasing.append(r)

            l=non_increasing[0]
            if l+k==r:
                non_increasing.popleft()
                l=non_increasing[0]
            
            if r>=k-1:
                res.append(nums[l])
            
                


           
        return res