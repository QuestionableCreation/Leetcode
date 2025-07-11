class Solution:

    def maxCoins(self, nums: List[int]) -> int:

        n = len(nums)
        score = [1] + nums + [1] 
        dp = [ [0] * (n + 2) for _ in range(n + 2) ]

        for j in range(n + 2):
            for i in range(j)[::-1]: 
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + score[i] * score[k] * score[j])

        return dp[0][n + 1]