class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]
        curr_str =""
        curr_num = 0
        i=0

        while i<len(s):
            
            
            if ord('a')<=ord(s[i])<=ord('z'):
                curr_str+= s[i]
            
            elif s[i]=='[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str=""
                curr_num=0
            
            elif s[i]==']':
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num*curr_str
            elif 0<= int(s[i])<=9:
                curr_num = curr_num*10 + int(s[i])
            i+=1
        return curr_str




        