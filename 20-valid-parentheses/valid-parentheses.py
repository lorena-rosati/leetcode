class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == "(" or p == "{" or p == "[":
                stack.append(p)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if (p == ")" and stack[-1] == "(") or (p == "]" and stack[-1] == "[") or (p == "}" and stack[-1] == "{"):
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0