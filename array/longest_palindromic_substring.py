class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for x in range(n)] for y in range(n)]

        max_length = 1
        start = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_length = 2

        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i + k -1

                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True

                    if k > max_length:
                        start = i
                        max_length = k

        return s[start:start + max_length] 