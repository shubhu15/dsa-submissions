class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt =Counter(nums)
        heap=[]
        for i,v in cnt.items():
            heapq.heappush(heap, (v, i))
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
            
        return res
        