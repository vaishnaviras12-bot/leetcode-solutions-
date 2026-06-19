#560. Subarray Sum Equals K
#Time complexity -O(n)
#space complexity O(n)
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        prefix_sum=0
        count=0
        for num in nums:
            prefix_sum+=num
            if prefix_sum-k in mp:
                count+=mp[prefix_sum-k]
            mp[prefix_sum]=mp.get(prefix_sum,0)+1
        return count
