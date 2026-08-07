class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,n+10):
            total=1
            num=i
            while num>0:
                digit=num%10
                total= total*digit
                num=num//10
            if total%t == 0:
                return i



        