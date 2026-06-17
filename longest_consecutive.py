#128. Longest Consecutive Sequence
#Time Complexity -O(n)
#Space complexity =  O(n)
from typing import List
class solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        num=set(nums)
        length=0

        for i in num:
            if i-1 not in num:
                length=1

                while i+length in num: 
                    length+=1

            longest=max(longest,length)
        return longest

