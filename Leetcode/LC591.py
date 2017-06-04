class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if code == '':
            return False
        stack = []
        word = ''
        i, n = 1, len(code)
        state = 0 # 0: start tag, 1: end tag, 2: text, 3: cdata 
        while i < n:
            #print i, state
            if state == 0:
                while i < n and code[i].isupper():
                    word += code[i]
                    i += 1
                if i >= n or code[i] != '>':
                    return False
                i += 1
                if len(word) > 9 or len(word) < 1: return False
                stack.append(word)
                word = ''
                if i >= n: return False
                if code[i] == '<':
                    i += 1
                    if i >= n: return False
                    if code[i] == '/':
                        i += 1
                        state = 1
                    elif code[i] == '!':
                        i += 1
                        state = 3
                    else:
                        state = 0
                    if i >= n: return False
                else:
                    state = 2
            elif state == 1:
                while i < n and code[i].isupper():
                    word += code[i]
                    i += 1
                if i >= n or code[i] != '>':
                    return False
                i += 1
                if stack[-1] != word:
                    return False
                stack.pop()
                word = ''
                if i >= n:
                    if len(stack) == 0: return True
                    else: return False
                if len(stack) == 0: return False
                if code[i] == '<':
                    i += 1
                    if i >= n: return False
                    if code[i] == '/':
                        i += 1
                        state = 1
                    elif code[i] == '!':
                        i += 1
                        state = 3
                    else:
                        state = 0
                    if i >= n: return False
                else:
                    state = 2
            elif state == 2:
                while i < n and code[i] != '<':
                    i += 1
                if i >= n: return False
                i += 1
                if i >= n: return False
                if code[i] == '/':
                    i += 1
                    state = 1
                elif code[i] == '!':
                    i += 1
                    state = 3
                else:
                    state = 0
                if i >= n: return False
            else: #state == 3
                if i+7 >= n or code[i:i+7] != '[CDATA[': return False
                i += 7
                j = code[i:].find(']]>')
                i += j+3
                if j == -1: return False
                if i >= n: return False
                if code[i] == '<':
                    i += 1
                    if i >= n: return False
                    if code[i] == '/':
                        i += 1
                        state = 1
                    elif code[i] == '!':
                        i += 1
                        state = 3
                    else:
                        state = 0
                    if i >= n: return False
                else:
                    state = 2
        return False
