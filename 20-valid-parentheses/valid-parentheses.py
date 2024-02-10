class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if len(stack) == 0 and (s[i] in [')',']','}']):
                return False
            elif s[i] in [')',']','}']:
                if s[i] == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(s[i])
        return stack == []