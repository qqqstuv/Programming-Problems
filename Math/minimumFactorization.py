# https://leetcode.com/contest/leetcode-weekly-contest-37/problems/minimum-factorization/

class Solution:
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a
        i = 9
        result = []
        while(a != 1):
            if a % i == 0:
                a =a / i
                result.append(i)
            else:
                i -= 1
                if i == 1 and a != 1:
                    return 0
        num = ""
        for i in reversed(result):
            print(i)
            num += str(i)
        num = int(num)
        if num > 2147483648:
            return 0
        return num