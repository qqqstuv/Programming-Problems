# Source: https://leetcode.com/problems/longest-palindrome/#/description
# Topics: @Hashmap, @Array
class Solution(object):
    def longestPalindrome(self, s):
        odds = sum(v & 1 for v in collections.Counter(s).values())
        return len(s) - odds + bool(odds)
