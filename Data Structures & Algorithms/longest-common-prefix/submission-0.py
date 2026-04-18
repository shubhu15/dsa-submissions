class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s1=strs[0]

        for s in strs[1:]:

            while len(s1)>0 and not s.startswith(s1):
                s1=s1[:-1]

        return s1
        