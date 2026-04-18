class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l= len(nums)
        k%=l
        
        def reverse(i,j):
            while i<j:
                nums[i], nums[j] = nums[j], nums[i]
                i,j = i+1, j-1
        
        reverse(0,l-1)
        reverse(0,k-1)
        reverse(k, l-1)