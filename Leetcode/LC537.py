class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = a.split('+')
        y = b.split('+')
        x1, x2 = int(x[0]), int(x[1][:-1])
        y1, y2 = int(y[0]), int(y[1][:-1])
        z1 = x1 * y1 - x2 * y2
        z2 = x1 * y2 + x2 * y1
        return str(z1)+'+'+str(z2)+'i'
