# Problem: Fibonacci Number
# Difficulty: Easy
# Approach: Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def fib(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        def solve(n):
            if n <= 1:
                return n
            
            if dp[n] != -1:
                return dp[n]
            
            dp[n] = solve(n-1) + solve(n-2)
            return dp[n]
        
        return solve(n)