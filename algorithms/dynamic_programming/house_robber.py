"""
    Created by Mustafa Sencer Özcan on 27.05.2020.

    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint stopping you from robbing each
    of them is that adjacent houses have security system connected and it will automatically contact the police if
    two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police.
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i < 2:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + max(dp[:i - 1])
        return max(dp)


if __name__ == '__main__':
    result = Solution().rob([2, 1, 1, 2, 7])
    print(result)
