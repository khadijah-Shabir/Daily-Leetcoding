from collections import Counter
from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Count elements in nums1
        counts = Counter(nums1)
        
        # Step 2: Find intersections with nums2
        result = []
        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        
        return result