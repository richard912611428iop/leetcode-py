class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = collections.deque()
        if s is None or len(s) == 0:
            return True
        stack.append(s[0])
        for i in range(1, len(s)):
            c = s[i]
            if c == '}':
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if a != '{':
                    return False
            elif c == ']':
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if a != '[':
                    return False
            elif c == ')':
                if len(stack) == 0:
                    return False
                a = stack.pop()
                if a != '(':
                    return False
            else:
                stack.append(c)
        if len(stack) != 0:
            return False
        return True
