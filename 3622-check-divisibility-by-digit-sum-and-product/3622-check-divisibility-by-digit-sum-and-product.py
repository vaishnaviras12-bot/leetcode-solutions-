class Solution:
    def checkDivisibility(self, n: int) -> bool:
        original =n 
        product =1
        total=0
        while n>0:
            digit = n%10
            total +=digit
            product *= digit 
            n=n//10
        if original%(total+product)==0:
            return True
        else:
            return False