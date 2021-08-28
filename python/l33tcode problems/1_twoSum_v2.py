class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary tracks values in num and thei index in the list
        indices = dict()
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in indices:
                return [indices[difference], i]
            indices[n] = i