class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        res = max(nums)
        temp_sub = 0
        for i in range(length):
            temp_sub += nums[i]
            res = max(temp_sub, res)
            if temp_sub < 0:
                temp_sub = 0
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1]
    print solution.maxSubArray(nums)
