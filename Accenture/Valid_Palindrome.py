class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=[]
        s=s.replace(" ", "")
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                l.append(s[i])
        new_s=''.join(l)
        temp=new_s
        new_s=new_s[::-1]
        if temp==new_s:
            return True
        return False

        
