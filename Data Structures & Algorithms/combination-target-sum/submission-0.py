class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]


        def back(i, curr_sum, curr):
            if curr_sum ==0:
                res.append(curr[:])
                return
            if curr_sum < 0 or i== len(nums):
                return
            
        
            curr.append(nums[i])

            back(i, curr_sum-nums[i], curr)
            curr.pop()
            back(i+1, curr_sum, curr)

        back(0, target, [])
        return res



        