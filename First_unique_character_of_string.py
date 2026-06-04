#387. First Unique Character in a String
#Time complexity: O(n)
#Space complexity: O(n)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count ={}
        for i,num in enumerate(s):
            count[num] = count.get(num,0)+1
        for i in range(len(s)):
            if count[s[i]]==1:
                return i
        return -1
        