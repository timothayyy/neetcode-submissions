class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, nums in enumerate(nums):
            complement = target - nums

            if complement not in seen:
                seen[nums] = i
            else:
                return [seen[complement], i]

