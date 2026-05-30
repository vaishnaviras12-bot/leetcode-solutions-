#26. Remove Duplicates from Sorted Array
#Time Complexity is O(n) and space complexity is O(1)
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[k-1]:
                nums[k]=nums[i]
                k+=1
        return k