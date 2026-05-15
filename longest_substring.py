class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        char_set = set()
        max_len = 0

        while right < len(s):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])

            max_len = max(max_len, right - left + 1)

            right += 1

        return max_len