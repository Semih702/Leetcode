class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        if nums[r]==target:
            return r
        if nums[l]==target:
            return l
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[r]:
                if nums[r]>=target or nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            elif nums[mid]<nums[r]:
                if target>nums[mid] and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1    
        return -1