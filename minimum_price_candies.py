#2144. Minimum Cost of Buying Candies With Discount
#Time Complexity: O(nlogn)
#Space Complexity: O(1)
from typing import List
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost)==1:
            return cost[0]
        cost.sort(reverse=True)
        min_price=0
        for i in range(len(cost)):
            if (i%3 != 2):
                min_price+=cost[i]
        return min_price

