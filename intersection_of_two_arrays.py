# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each
# element in the result must be unique and you may return the result in any order.
# Time Complexity: O(n + m) where n and m are the lengths of nums1 and nums2 respectively.
# Space Complexity: O(n + m) in the worst case when all elements are unique in both arrays.
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)& set(nums2))