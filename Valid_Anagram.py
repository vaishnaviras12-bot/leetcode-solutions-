#242. Valid Anagram
#Time Complexity : O(2n)
#Space Complexity : O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count ={}
        for i in s:
            count[i] = count.get(i,0)+1
        for i in t:
            if i not in count:
                return False
            count[i]-=1
            if count[i]<0:
                return False
        return True
    