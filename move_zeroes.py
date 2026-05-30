# 283. Move Zeroes
#we are modyfing the array in place and we are not returning anything
#Time Complexity is O(n) and space complexity is O(1)
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1



