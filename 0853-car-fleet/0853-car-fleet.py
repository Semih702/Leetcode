class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        position,speed=zip(*sorted(zip(position, speed),reverse=True))
        
        fleet=1
        current=(target-position[0])/speed[0]

        for i,j in zip(position[1:],speed[1:]):
            temp=(target-i)/j
            if temp>current:
                fleet+=1
                current=temp
        return fleet
        
        

        