class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i=0
        r= len(numbers)-1
        while i<r:
            s= numbers[i]+ numbers[r]
            if s==target:
                return [i+1, r+1]
            elif s>target:
                r=r-1
            else:
                i=i+1
        return [-1,-1]
        