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
        flag = True
        for i in range(0, length, 2):
            if self.s[i+1] != prnts[self.s[i]]:
                flag = False
        return flag


par = Solution("(}")
print(par.parentheses())
