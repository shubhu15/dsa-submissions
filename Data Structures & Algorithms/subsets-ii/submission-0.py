class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()

        def back(curr, i):
            if i==len(nums):
                res.add(tuple(curr[:]))
                return
            
            
            curr.append(nums[i])
            back(curr, i+1)
            curr.pop()
            back(curr, i+1)

        back([],0)
        return [list(l) for l in res]

        