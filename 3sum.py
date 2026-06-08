#3 sum
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#Notice that the solution set must not contain duplicate triplets.
#Time Complexity : O(n^2) where n is the length of the input array. This is because we have two nested loops: the outer loop runs n times, and the inner loop runs at most n times in total across all iterations of the outer loop.
#Space Complexity : O(1) if we don't consider the space used for the output list. The sorting step takes O(log n) space, but the output list can take up to O(n^2) space in the worst case if there are many triplets that sum to zero.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while k>j:
                total= nums[i]+nums[j]+nums[k]
                if total ==0:
                    result.append([nums[i],nums[j],nums[k]]) 
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif total < 0:
                    j+=1
                elif total >0:
                    k-=1
        return result 
                                