class Solution:
    def maximumWealth(self, nums: List[List[int]]) -> int:
        result=[]
        sum1=0
        for i in range (len(nums)):
            add=sum(nums[i])
            result.append(add)
        maximum=max(result)
        return maximum
        
                
        