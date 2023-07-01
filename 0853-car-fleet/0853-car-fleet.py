class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time=[]
        for i,j in enumerate(position):
            time.append((target-j)/speed[i])
        position,time=zip(*sorted(zip(position, time),reverse=True))
        
        fleet=1
        current=time[0]

        for i in time[1:]:
            if current and i>current:
                fleet+=1
                current=i
        return fleet
        
        

        