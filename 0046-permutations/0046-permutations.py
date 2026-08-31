class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def backtrack(curr):
            if len(nums)==len(curr):
                result.append(curr.copy())
                return
            for i in range(len(nums)):
                if nums[i] in curr:
                    continue
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()

        backtrack([])
        return result