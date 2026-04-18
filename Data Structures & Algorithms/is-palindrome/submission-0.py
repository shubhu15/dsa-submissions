class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_s=""
        for i in s:
            if i.isalnum():
                new_s+=i
        
        return new_s==new_s[::-1]
        