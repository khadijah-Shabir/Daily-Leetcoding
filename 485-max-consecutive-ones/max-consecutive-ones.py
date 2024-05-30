from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # To store the maximum number of consecutive 1's
        current_count = 0  # To count the current number of consecutive 1's
        
        for num in nums:
            if num == 1:
                current_count += 1  # Increment current count if the number is 1
                max_count = max(max_count, current_count)  # Update max count if needed
            else:
                current_count = 0  # Reset current count if the number is 0
                
        return max_count