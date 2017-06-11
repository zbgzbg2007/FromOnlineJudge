class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.i = 0
        self.s = compressedString
        self.count = 0


    def next(self):
        """
        :rtype: str
        """
        if self.hasNext() == False:
            return ' '
        self.count -= 1
        x = self.s[self.i]
        if self.count == 0:
            j = self.i+1
            while j < len(self.s) and self.s[j].isdigit():
                j += 1
            self.i = j
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.i >= len(self.s):
            return False
        if self.count == 0:
            j = self.i+1
            while j < len(self.s) and self.s[j].isdigit():
                j += 1
            self.count = int(self.s[self.i+1:j])
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
