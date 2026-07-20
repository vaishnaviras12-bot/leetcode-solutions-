#875. Koko Eating Bananas
#Time complexity - O(n log m) where n is the number of piles and m is the maximum number of bananas in a pile
#Space complexity - O(1)
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal(mid):
            i=0
            hour=0
            while i<len(piles):
                hour+= (piles[i] + mid -1)//mid
                i+=1
            return hour
        low=1
        high=max(piles)
        ans=high
        while low<=high:
            mid=(low+high)//2
            hrs= cal(mid)
            if hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans