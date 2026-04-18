class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxh= []
        i=0
        res=[]
        for j in range(len(nums)):
            heapq.heappush(maxh, (-nums[j], j))

            if j>=k-1:
                while maxh[0][1]<=j-k:
                    heapq.heappop(maxh)
                res.append(-maxh[0][0])
            

        return res



            
        