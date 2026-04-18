class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)

        for i in range(n):
            min_i= i
            for j in range(i, n):
                if nums[j]<nums[min_i]:
                    min_i=j
            nums[min_i], nums[i]=nums[i], nums[min_i]
        return nums

        