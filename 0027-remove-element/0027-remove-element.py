class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left_shift=0
        
        for i in range(len(nums)):
            if nums[i]==val:
                left_shift+=1
            else:
                nums[i-left_shift]=nums[i]
                
        for _ in range(left_shift):
            nums.pop()