class Solution:
    def __init__(self, s):
        self.s = s
    def parentheses(self):
        prnts = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        length = len(self.s)
        stack = []
        for i in range(length):
            if self.s[i] in prnts:
                stack.append(self.s[i])
            elif not stack or prnts[stack.pop()] != self.s[i]:
                return False
        return len(stack) == 0


par = Solution("(}")
print(par.parentheses())