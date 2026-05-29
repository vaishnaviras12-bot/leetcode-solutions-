# Problem: Longest Substring Without Repeating Characters
# Difficulty: Medium
#
# Approach:
# This problem is solved using the Sliding Window technique.
#
# We maintain:
# - a left pointer
# - a right pointer
# - a set to store unique characters in the current window
#
# The right pointer expands the window.
# If a duplicate character is found, we shrink the window
# from the left side until the duplicate is removed.
#
# At every step, we calculate the current window length
# and update the maximum length found so far.
#
# Time Complexity: O(n)
# Each character is added and removed from the set at most once.
#
# Space Complexity: O(min(n, m))
# where m is the character set size.
#
# Example:
# Input: "abcabcbb"
# Output: 3
# Explanation:
# The longest substring without repeating characters is "abc".
class Solution:
    def lengthOfLongestSubstring(self,s):

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
