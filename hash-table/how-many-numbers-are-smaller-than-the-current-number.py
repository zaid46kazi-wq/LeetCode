from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        smaller_count = {}

        # Store first occurrence index
        for index, num in enumerate(sorted_nums):
            if num not in smaller_count:
                smaller_count[num] = index

        # Build result
        return [smaller_count[num] for num in nums]