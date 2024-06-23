class RemoveElement:
    def __init__(self, val):
        self.val = val
        self.nums = []
    def remove_element(self, nums):
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == self.val:
                nums[i] = None
                k -= 1
        nums = sorted(nums, key=lambda x: x is None)
        # when element equals to None, x gives True
        return k, nums


n = RemoveElement(3)
print(n.remove_element([3, 2, 2, 3]))
