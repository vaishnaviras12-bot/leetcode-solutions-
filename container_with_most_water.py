#167. Container With Most Water
#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        k=0
        while right>left:
            area=min(height[left],height[right])*(right-left)
            k=max(k,area)

            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return k
        