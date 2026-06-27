#724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        l=0
        for i in range(len(nums)):
            l+=nums[i]
            if total-l == l-nums[i]:
                return i
        return -1

        