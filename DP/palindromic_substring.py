#https://leetcode.com/problems/palindromic-substrings/description/
#Just a review question
class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        count = 1 # single last character as I loop through (len(s) - 1) character only
        for idx in range(len(s) - 1):
            p1 = idx
            p2 = idx
            while s[p1] == s[p2]:
                count += 1
                if p1 - 1 >= 0 and p2 + 1 < len(s):
                    p1 -= 1
                    p2 += 1
                else:
                    break
            p1 = idx
            p2 = idx + 1
            while s[p1] == s[p2]:
                count += 1
                if p1 -1 >= 0 and p2 + 1 < len(s):
                    p1 -= 1
                    p2 += 1
                else:
                    break
        return count