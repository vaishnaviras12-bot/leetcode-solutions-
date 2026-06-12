#49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Time: O(m * n * log(n)) where m is the number of strings and n is the average length of each string
# Space: O(m * n)

from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        return list(d.values())