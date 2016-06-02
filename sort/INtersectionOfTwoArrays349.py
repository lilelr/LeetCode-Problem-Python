class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type:  List[int]
        """
        return [x for x in set(nums1) if x in set(nums2)]
