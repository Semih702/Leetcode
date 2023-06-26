class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        fullist=sorted(nums1+nums2)
        if len(fullist)%2==1:
            return(fullist[int(len(fullist)/2-0.5)])
        else:
            
            return((fullist[int(len(fullist)/2)]+fullist[int(len(fullist)/2-1)])/2)