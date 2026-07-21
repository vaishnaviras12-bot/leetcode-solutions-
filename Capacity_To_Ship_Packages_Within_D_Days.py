#1011. Capacity To Ship Packages Within D Days
#Time Complexity: O(nlog(sum(weights)-max(weights)))
#Space Complexity: O(1)
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def d(mid):
            days_required=1
            current_weight=0
            for weight in weights:
                if current_weight+weight>mid:
                    current_weight=weight
                    days_required+=1
                else:
                    current_weight+=weight
            return days_required
    

        low= max(weights)
        high = sum(weights)
        while low<high:
            mid=(high+low)//2
            c=d(mid)
            if c<=days:
                high=mid
            else:
                low=mid+1
        return low

