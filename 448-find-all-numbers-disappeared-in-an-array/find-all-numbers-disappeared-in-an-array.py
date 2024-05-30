class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num_set=set(range (1, n+1))
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        return list(num_set)
        