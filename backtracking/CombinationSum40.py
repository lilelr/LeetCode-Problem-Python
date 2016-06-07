import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :param candidates:
        :param target:
        :return:
        """
        res = []
        candidates = sorted(candidates)
        templist = []
        self.backtracking(target, candidates, 0, res, templist)
        return res

    def backtracking(self, remain, nums, start, res, tempList):
        if remain == 0:
            res.append(copy.copy(tempList))
            return
        elif remain < 0:
            return
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tempList.append(nums[i])
                self.backtracking(remain - nums[i], nums, i + 1, res, tempList)
                tempList.pop()
            return


if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    res = solution.combinationSum2(candidates, target)
    print 'fe'
    for itemList in res:
        for item in itemList:
            print str(item),
        print
