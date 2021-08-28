# Runtime: 52 ms, faster than 96.16% of Python3 online submissions for Two Sum.
# Memory Usage: 15.3 MB, less than 53.83% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary tracks values in num and thei index in the list
        indices = dict()
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in indices:
                return [indices[difference], i]
            indices[n] = i