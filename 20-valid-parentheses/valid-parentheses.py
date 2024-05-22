class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        stack = []
        for c in s:
            l = len(stack)
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if l == 0:
                    return False
                else:
                    if c == ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    elif c == "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    elif c == "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
        
        return len(stack) == 0