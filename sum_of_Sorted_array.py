#977. Squares of a Sorted Array
#Time Complexity = O(n)
#Space Complexity = O(n)
from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr=[-1]*len(nums)
        head=0
        pivot=len(arr)-1
        tail=len(nums)-1
        while head <=tail:
            if nums[head]*nums[head]>nums[tail]*nums[tail]:
                arr[pivot] = nums[head]*nums[head]
                head+=1
            else:
                arr[pivot] = nums[tail]*nums[tail]
                tail-=1
            pivot-=1
        return arr
        
        