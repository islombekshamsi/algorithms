class Solution:
    def __init__(self, number):
        self.number = number

    def palindrome(self):
        length = len(str(self.number))
        top = length - 1
        flag = True  # Change the initial value of flag to True
        for i in range(length // 2):  # Iterate only till half of the length
            if str(self.number)[i] != str(self.number)[top]:  # Check for inequality
                flag = False
                break
            top -= 1
        return flag


number = Solution(12241)
print(number.palindrome())
