class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAltitude=0
        maxAltitude=0
        for i in range(len(gain)):
            currAltitude+=gain[i]
            maxAltitude=max(currAltitude,maxAltitude)
        if maxAltitude>0:
            return maxAltitude
        return 0


        
        