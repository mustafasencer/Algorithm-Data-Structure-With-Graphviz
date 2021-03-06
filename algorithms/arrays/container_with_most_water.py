"""
    Created by Mustafa Sencer Özcan on 20.05.2020.

    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
    n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
    Find two lines, which together with x-axis forms a container, such that the container contains the most water.

    Note: You may not slant the container and n is at least 2.
"""
from typing import List


class Solution:
    def max_area(self, height: List[int]) -> int:
        max_area = 0
        j = len(height) - 1
        i = 0
        while i != j:
            if height[i] > height[j]:
                max_area = max(height[j] * (j - i), max_area)
                j -= 1
            else:
                max_area = max(height[i] * (j - i), max_area)
                i += 1
        return max_area


if __name__ == '__main__':
    result = Solution().max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
    print(result)
