# 49. Group Anagrams
# frequency count+ tuple as key
# Time: O(m * n) where m is the number of strings and n is the average length of each string
# Space: O(m * n)
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            d[tuple(count)].append(s)
        return list(d.values())