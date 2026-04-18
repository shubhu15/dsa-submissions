class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxk = max(piles)
        res=maxk
        mink=1

        while mink<=maxk:
            k = mink + (maxk- mink)//2
            
            tt=0
            for p in piles:
                tt += math.ceil(p/k)
            if tt<=h:
                maxk=k-1
            else:
                mink=k+1
        return mink