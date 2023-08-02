class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size=len(nums1)+len(nums2)
        low,high=nums1,nums2
        if len(low)>len(high):
            low,high=high,low
        mid=size//2
        l,r=0,len(low)-1
        while True:
            leftmid=(l+r)//2
            rightmid=mid-leftmid-2

            lowleft= low[leftmid] if leftmid>=0 else float("-inf")
            lowright= low[leftmid+1] if leftmid+1<len(low) else float("inf")
            highleft= high[rightmid] if rightmid>=0 else float("-inf")
            highright= high[rightmid+1] if rightmid+1<len(high) else float("inf")

            if lowleft<=highright and highleft<=lowright:
                if size%2:
                    return min(lowright,highright)
                return (max(lowleft,highleft)+min(lowright,highright))/2
            elif lowleft<=highright:
                l=leftmid+1
            else:
                r=leftmid-1
                
