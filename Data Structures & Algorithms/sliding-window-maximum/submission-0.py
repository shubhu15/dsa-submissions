class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxq= deque()
        i=0
        res=[]

        for j in range(k):
            while maxq and maxq[-1]<nums[j]:
                maxq.pop()
            maxq.append(nums[j])
        res.append(maxq[0])

        for j in range(k,len(nums)):

            if j-i+1>k:
                if nums[i]== maxq[0]:
                    maxq.popleft()
                i+=1
            while maxq and maxq[-1]<nums[j]:
                maxq.pop()
            maxq.append(nums[j])
            res.append(maxq[0])
        return res



            
        