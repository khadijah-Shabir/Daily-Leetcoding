class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red=white=blue=0
        for i in nums:
            if i == 0:
                red+=1
            elif i ==1:
                white+=1
            else:
                blue+=1
        nums[:]= red*[0]+white*[1]+blue*[2]
        