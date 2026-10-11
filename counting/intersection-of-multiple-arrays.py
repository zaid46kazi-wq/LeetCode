class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        result = []

        for num in nums[0]:
            count = 0

            for arr in nums:
                if num in arr:
                    count += 1

            if count == len(nums):
                result.append(num)

        return sorted(result)