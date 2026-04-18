class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap={}
        for i,j in enumerate(nums):
            if target-j in hmap:
                return [hmap[target-j], i]
            hmap[j]=i

        return




        