class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = dict()
        for val in nums1:
            if val not in dict1:
                dict1[val] = 1
            else:
                dict1[val] += 1
        ret = []
        for val in nums2:
            if val in dict1 and dict1[val] > 0:
                ret.append(val)
                dict1[val] -= 1
        return ret

    def intersect2(self, nums1, nums2):
        result = []
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                nums2.remove(nums1[i])
                result.append(nums1[i])
        return result
