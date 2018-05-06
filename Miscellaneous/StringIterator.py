# Source: https://leetcode.com/contest/leetcode-weekly-contest-36/problems/design-compressed-string-iterator/
# Topics: @Array, @Hashmap 
class StringIterator:
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.compressed = []
        letter = None
        occur = ''
        char = ''
        for idx, val in enumerate(compressedString):
            print(val)
            if val.isdigit():
                occur += val
                if idx == len(compressedString) -1:
                    self.compressed.append([char, int(occur)])
            else:
                if char != '':
                    self.compressed.append([char, int(occur)])
                    occur = ''
                char = val
        self.pointer = 0
        print(self.compressed)
    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return ' '
        if self.compressed[self.pointer][1] != 0:
            self.compressed[self.pointer][1] -= 1
            return str(self.compressed[self.pointer][0])
        else:
            self.pointer += 1
            return self.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer == len(self.compressed) - 1 and self.compressed[self.pointer][1] == 0:
            return False
        return True
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
