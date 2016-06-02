class Solution(object):


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :return: bool
        """

        d1 = {}
        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1

        for i in t:
            if i not in d1:
                return False
            else:
                d1[i] -= 1

        for key in d1:
            if d1[key] != 0:
                return False
        return True
