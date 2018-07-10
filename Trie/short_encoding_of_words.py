#https://leetcode.com/problems/short-encoding-of-words/description/
class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()
        
    def insert(self, word):
        if word:
            if word[0] not in self.children:
                self.children[word[0]] = Node(word[0])
            self.children[word[0]].insert(word[1:])
            
    def traverse_get_all_length(self,current_height): # traverse get all length from root to leaf node
        if not self.children:
            return  current_height + 1 # +1 for the #
        total = 0
        for key, val in self.children.items():
            total += val.traverse_get_all_length(current_height + 1)
        return total
    
    def print(self):
        print(self.val, list(self.children.keys()))
        for key,val in self.children.items():
            val.print()
        
class Solution:
    
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        root = Node("")
        for word in words:
            root.insert(word[::-1])
        # root.print()
        total = root.traverse_get_all_length(0)
        return total