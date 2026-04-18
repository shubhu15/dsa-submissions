class TimeMap:

    def __init__(self):
        self.hmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.hmap[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        
        val_list= self.hmap[key]
        i=0
        l= len(val_list)-1
        res=""
        while i<=l:
            mid = i+ (l-i)//2
            if val_list[mid][0]<= timestamp:
                res=val_list[mid][1]
                i=mid+1           
            else:
                l=mid-1
        return res if len(res)>0 else ""

        
