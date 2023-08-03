class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow,fast=nums[0],nums[nums[0]]
        
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        left=0
        while left!=slow:
            left=nums[left]
            slow=nums[slow]
        return left
            