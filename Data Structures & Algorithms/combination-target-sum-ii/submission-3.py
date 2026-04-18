class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res=[]
        candidates.sort()

        def back(i, curr_s, curr):
            if curr_s == 0:
                res.append(curr[:])
                return
            if curr_s<0 or i== len(candidates):
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if curr_s + candidates[j]<0:
                    return
                curr.append(candidates[j])
                back(j+1, curr_s- candidates[j], curr )
                curr.pop()

        back(0, target, [])
        return res