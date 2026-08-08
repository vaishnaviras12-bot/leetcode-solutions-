class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _hash={0:-1}
        balance=0
        maximum=0
        for i in range(len(nums)):
            if nums[i]==0:
                balance -=1
            else:
                balance += 1
            if balance in _hash:
                maximum =max(maximum,i-_hash[balance])
            else:
                _hash[balance]= i
        return maximum

                

        