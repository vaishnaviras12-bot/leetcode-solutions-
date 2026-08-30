class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(index,current):
            result.append(current.copy())
            for i in range(index,len(nums)):
                current.append(nums[i])
                backtracking(i+1,current)
                current.pop()
        backtracking(0,[])
        return result