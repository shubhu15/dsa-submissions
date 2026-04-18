class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hmap={}

        for i in range(len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]]=i
            else:
                j = hmap[nums[i]]
                if abs(j-i)<=k:
                    return True
                else:
                    hmap[nums[i]]=i
        return False
        