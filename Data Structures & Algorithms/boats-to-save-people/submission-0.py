class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        i=0
        j=len(people)-1
        nums=0

        while i<=j:

            s = people[i]+people[j]
            if s>limit:
                nums+=1
                j-=1
            else:
                nums+=1
                i+=1
                j-=1
        return nums

        