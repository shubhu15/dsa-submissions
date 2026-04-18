class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hmap =Counter(nums)

        for i,j in hmap.items():
            if j> len(nums)//2:
                return i

            
        