class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
# Initialize a 1D DP array with 1s
        dp = [1] * n
        
        # Update the DP array for each row
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        # Return the number of unique paths to the bottom-right corner
        return dp[n-1]