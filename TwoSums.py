class Solution:
    def __init__(self, nums: list[int], target: int):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for index in range(len(self.nums) - 1):
            if self.nums[index] + self.nums[index + 1] == self.target:
                return [index, index + 1]
        return []
