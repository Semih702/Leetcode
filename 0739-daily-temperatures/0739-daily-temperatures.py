class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        days=[]
        for i,j in enumerate(temperatures):
            while days and j>days[-1][0]:
                if days[-1][0]<j:
                    res[days[-1][1]]=i-days[-1][1]
                    days.pop()
            days.append((j,i))
            
        return res
        