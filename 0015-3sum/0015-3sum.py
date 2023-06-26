class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for j,i in enumerate(nums):
            p1=j+1
            p2=len(nums)-1
            if j>0 and i==nums[j-1]:
                continue
            while p2>p1:
                temp=nums[p1]+nums[p2]                
                if temp==-i:
                    result.append([i,nums[p1],nums[p2]])
                    p2-=1
                    while nums[p2]==nums[p2+1] and p2>p1:
                        p2-=1 
                    p1+=1
                    while nums[p1]==nums[p1-1] and p2>p1:
                        p1+=1
                elif temp>-i:
                    p2-=1
                else:
                    p1+=1
        return result    
