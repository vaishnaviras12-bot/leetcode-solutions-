class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result =[]
        def backtrack(arr,start):
            if sum(arr)>target:
                return
            if sum(arr) == target:
                result.append(arr.copy())
                return
            for i in range(start,len(candidates)):
                arr.append(candidates[i])
                backtrack(arr,i)
                arr.pop()
        backtrack([],0)
        return result
