from typing import List

# Backward DP scan: O(n^2) time, O(n) space
class SolutionBackward:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # If the list is empty, there's no subsequence
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n  # Each element alone is a subsequence of length 1

        # Iterate from the end of the list to the beginning
        for i in range(n - 1, -1, -1):
            # For each i, look at every element after it
            for j in range(i + 1, n):
                # If nums[j] can extend the sequence from nums[i]
                if nums[j] > nums[i]:
                    # Then we can form a subsequence with j.
                    dp[i] = max(dp[i], dp[j] + 1)
                  
        return max(dp)


# Forward DP scan: O(n^2) time, O(n) space
class SolutionForward:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # If the list is empty, no subsequence exists
        if not nums:
            return 0

        n = len(nums)
        # dp[i] will hold the length of the longest increasing subsequence ending at index i
        dp = [1] * n  # Each element alone forms a length-1 subsequence

        # Build up dp from left to right
        for i in range(1, n):
            # For the current position i, check all previous positions j < i
            for j in range(i):
                # If nums[i] extends the sequence that ended at j
                if nums[i] > nums[j]:
                    # Then we can form a subsequence with j.
                    dp[i] = max(dp[i], dp[j] + 1)

        
        return max(dp)
