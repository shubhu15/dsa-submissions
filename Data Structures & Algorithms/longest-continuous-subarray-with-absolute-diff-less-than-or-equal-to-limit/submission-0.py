class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        maxq = deque()
        minq = deque()
        res=0
        i=0

        for j in range(len(nums)):
            while minq and minq[-1]>nums[j]:
                minq.pop()
            while maxq and maxq[-1]<nums[j]:
                maxq.pop()
            minq.append(nums[j])
            maxq.append(nums[j])


            while maxq[0] - minq[0]>limit:
                if maxq[0]==nums[i]:
                    maxq.popleft()
                if minq[0]==nums[i]:
                    minq.popleft()
                i+=1
            res= max(res, j-i+1)

        return res
        