# Runtime: 3445 ms, faster than 29.28% of Python3 online submissions for Two Sum.
# Memory Usage: 14.8 MB, less than 80.63% of Python3 online submissions for Two Sum.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        # 1. Loop through nums
        # 2. Find difference between current value in nums and target
        # 3. Loop through nums starting from the next linear index value
        # 4. If the current value of num equals difference, return the indices of both
        for x in range(len(nums)):
            difference = target - nums[x]
            for y in range(x+1, len(nums)):
                if nums[y] == difference:
                    return [x,y]              