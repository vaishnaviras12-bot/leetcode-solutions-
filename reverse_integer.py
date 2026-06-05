#7. Reverse Interger
class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        int_max=2**31-1
        int_min=-2**31
        sign=-1 if x<0 else 1
        x=abs(x)
        while x!=0:
            digit=x%10
            x=x//10
            if rev>(int_max - digit)//10 :
                return 0
                
            rev=rev*10+digit
        return sign*rev
        