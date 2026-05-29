#Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution:
    def maxSubArray(self, nums):
        max_sum = float('-inf')
        current_sum = 0

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum