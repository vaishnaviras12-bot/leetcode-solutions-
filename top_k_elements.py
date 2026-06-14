#347. Top K Frequent Elements
# Given a non-empty array of integers, return the k most frequent elements.
# Time: O(n log n) where n is the number of unique elements in the array
# Space: O(n) where n is the number of unique elements in the array
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _hash={}
        for i in nums:
            if i in _hash:
                _hash[i]+=1
            else:
                _hash[i]=1
        sorted_d= sorted(_hash.items() ,key =lambda x: x[1] ,reverse =True)
        return [item[0] for item in sorted_d[:k]]