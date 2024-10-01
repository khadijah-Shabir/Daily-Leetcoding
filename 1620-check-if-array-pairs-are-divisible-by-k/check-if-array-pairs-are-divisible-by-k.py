from collections import defaultdict

class Solution:
    def canArrange(self, arr, k):
        # Create a map to store the frequency of each remainder
        remainderMap = defaultdict(int)

        # Iterate over the array and calculate the remainder of each element mod k
        for num in arr:
            rem = num % k
            if rem < 0:
                rem += k  # Handle negative remainders
            
            # Increment the frequency of the remainder
            remainderMap[rem] += 1

        # Now check if all remainders can be paired correctly
        for rem, count in remainderMap.items():
            if rem == 0:  # Special case: remainder 0 must have an even count
                if count % 2 != 0:
                    return False
            else:
                complement = k - rem
                # Check if the count of remainder rem matches the count of its complement
                if remainderMap[rem] != remainderMap[complement]:
                    return False
        
        return True
