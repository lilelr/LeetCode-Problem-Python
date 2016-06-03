"""
Radix Sort
https://leetcode.com/discuss/75646/radix-sort-in-python
Radix sort, you can see the explanation follow the links.
https://www.cs.usfca.edu/~galles/visualization/RadixSort.html
"""


def maximumGap(nums):
    if not nums:
        return 0

    max_num = max(nums)
    bucket = [[] for i in range(10)]
    exp = 1
    while max_num / exp > 0:
        for num in nums:
            bucket[(num / exp) % 10].append(num)
        nums = []
        for each in bucket:
            nums.extend(each)
        bucket = [[] for i in range(10)]
        exp *= 10

    max_gap = 0
    for i in range(1, len(nums)):
        max_gap = max(max_gap, nums[i] - nums[i - 1])
    return max_gap


if __name__ == '__main__':
    nums = [105, 7, 5]
    res = maximumGap(nums)
    print [[] for i in range(10)]
