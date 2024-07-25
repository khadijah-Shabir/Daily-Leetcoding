class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count=0
        dict={}
        for num in nums:
            if num in dict: 
                count+=dict[num] 
                dict[num]+=1
            else: 
                dict[num]=1
        return count


        