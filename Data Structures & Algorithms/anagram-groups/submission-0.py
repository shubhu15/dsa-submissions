class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap=defaultdict(list)

        for word in strs:
            freq=[0]*26
            for w in word:
                freq[ ord(w)- ord('a')]+=1
            key = tuple(freq)
            hmap[key].append(word)
        

        res=[]
        for k,v in hmap.items():
            res.append(v)
        return res


        

        