class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_set = set(nums)
        
        # Convert set back to list
        unique_list = list(unique_set)
        
        # Sort the unique list to maintain order
        unique_list.sort()
        
        # Replace the elements in the original list with elements from the unique list
        for i in range(len(unique_list)):
            nums[i] = unique_list[i]
        
        # Return the length of the unique list
        return len(unique_list)
        
        