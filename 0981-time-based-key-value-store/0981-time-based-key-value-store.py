class TimeMap:

    def __init__(self):
        self.times=[]
        self.keys=defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times.append(timestamp)
        self.keys[timestamp][key]=value

    def get(self, key: str, timestamp: int) -> str:
        l,r=0,len(self.times)-1
        mid=(l+r)//2
        while l<=r:
            if self.times[mid]==timestamp:
                break
            if self.times[mid]<timestamp:
                l=mid+1
            else:
                r=mid-1
            mid=(l+r)//2

        while mid>=0:
            if self.keys[self.times[mid]].get(key,""):
                return self.keys[self.times[mid]][key]
            mid-=1
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)