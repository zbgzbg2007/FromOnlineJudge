class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if expression[0] != '-':
            expression = "+"+expression
        i, a, b = 0, 0, 1
        for j in range(2, 11):
            b *= j
        while i < len(expression):
            pos = True
            if expression[i] == '-':
                pos = False
            i += 1
            if expression[i+1] == '/':
                x = int(expression[i])
                i += 2
            else:
                x = int(expression[i:i+2])
                i += 3
            if i+1 < len(expression) and expression[i+1] == '0':
                y = int(expression[i:i+2])
                i += 2
            else:
                y = int(expression[i])
                i += 1
            x *= b/y
            if pos: a += x
            else: a -= x
        for j in range(10, 1, -1):
            while a != 0 and b != 0 and a % j == 0 and b % j == 0:
                a /= j
                b /= j
        if a == 0: b = 1
        return str(a)+'/'+str(b)
        
