#567. Permutation in String
#optimized solution using sliding window and frequency count
#Time complexity: O(n)
#Space complexity: O(1) since we are using fixed size arrays of length 26
class Solution:
    def checkInclusion(self, s1: str , s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        count_s1 = [0]*26
        window_count =[0]*26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord('a')]+=1
            window_count[ord(s2[i])-ord('a')]+=1
        if count_s1 == window_count:
            return True
        for i in range(len(s1),len(s2)):
            window_count[ord(s2[i])-ord('a')]+=1
            window_count[ord(s2[i-len(s1)])-ord('a')]-=1
            if count_s1 == window_count:
                return True
        return False