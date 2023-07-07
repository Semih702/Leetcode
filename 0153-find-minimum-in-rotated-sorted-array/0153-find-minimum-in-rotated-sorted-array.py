class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=float("inf")
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid-1
            res=min(res,nums[mid])
        return res