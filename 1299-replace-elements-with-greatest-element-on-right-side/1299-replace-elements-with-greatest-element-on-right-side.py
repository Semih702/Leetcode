class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        
        for i in range(len(arr)-1,-1,-1):
            temp = greatest
            greatest = max(greatest , arr[i])
            
            arr[i] = temp
        return arr