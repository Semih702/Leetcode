class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        
        maxarea=0
        for i,j in enumerate(heights):
            index=i
            while stack and stack[-1][0]>j:
                height,index=stack.pop()
                maxarea=max(maxarea,(i-index)*height)
            stack.append((j,index))
            
        for i in stack:
            maxarea=max(maxarea,(i[0]*(len(heights)-i[1])))
        
        return maxarea