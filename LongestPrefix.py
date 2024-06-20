class Solution:
    def __init__(self):
        self.strs = []
    def longestprefix(self, strs):
        res = ""
        for i in range(len(strs[0])):
            for z in strs:
                if i == z or z[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res


words = Solution()
print(words.longestprefix(["flowers", "flour", "flight"]))
