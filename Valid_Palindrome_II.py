#680. Valid Palindrome II
#Time Complexity : O(n)
#Space Complexity : O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s) - 1

        while a < b:
            if s[a] != s[b]:

                remove_left = s[:a] + s[a+1:]
                remove_right = s[:b] + s[b+1:]

                return (
                    remove_left == remove_left[::-1]
                    or
                    remove_right == remove_right[::-1]
                )

            a += 1
            b -= 1

        return True