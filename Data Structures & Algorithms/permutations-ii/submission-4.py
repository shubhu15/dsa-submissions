class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def back(i):                       # i = current position to fill
            if i == len(nums):             # <- fixed base case
                res.append(nums[:])
                return

            hset = set()

            for j in range(i, len(nums)):
                if nums[j] in hset:
                    continue               # skip duplicates at this depth
                hset.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]   # swap
                back(i + 1)
                nums[i], nums[j] = nums[j], nums[i]   # swap back

        back(0)
        return res

        