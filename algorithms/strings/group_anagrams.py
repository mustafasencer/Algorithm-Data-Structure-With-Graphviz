"""
    Created by Mustafa Sencer Özcan on 21.05.2020.
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for item in strs:
            sort_ = "".join(sorted(item))
            if sort_ in memo:
                memo[sort_].append(item)
            else:
                memo[sort_] = [item]
        result = [v for k, v in memo.items()]
        return result


if __name__ == '__main__':
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
