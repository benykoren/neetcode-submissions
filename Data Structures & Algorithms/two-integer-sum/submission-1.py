class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a_val in enumerate(nums):
            first = a_val
            for j, b_val in enumerate(nums):
                if a_val + b_val == target and i != j:
                    return [i, j]
        