#724. Find Pivot Index
# Given an array of integers nums, calculate the pivot index of this array.
# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum =total -left_sum -nums[i]

            if right_sum == left_sum:
                return i
    
            left_sum+=nums[i]
        return -1

