class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hset = set(nums)
        maxc=0

        for i in nums:
            if i-1 not in hset:
                count=1
                while i+count in hset:
                    count+=1
                maxc = max(maxc, count)


        return maxc
        