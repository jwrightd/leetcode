class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefs = [0] * n
        self.prefs[0] = nums[0]
        idx = 1
        while idx < n:
            self.prefs[idx] = self.prefs[idx - 1] + nums[idx]
            idx += 1
        print(self.prefs)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefs[right] - self.prefs[left - 1] if left - 1 >= 0 else self.prefs[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
