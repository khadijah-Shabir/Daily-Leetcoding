from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def rob_from(i: int) -> int:
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            if i == 0:
                return nums[0]
            
            # Compute the result and store it in memo
            memo[i] = max(rob_from(i - 1), nums[i] + rob_from(i - 2))
            return memo[i]
        
        return rob_from(len(nums) - 1)
