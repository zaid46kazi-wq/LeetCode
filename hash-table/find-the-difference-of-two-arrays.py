class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        set1 = set(nums1)
        set2 = set(nums2)

        only_in_nums1 = set1 - set2
        only_in_nums2 = set2 - set1

        return [list(only_in_nums1), list(only_in_nums2)]