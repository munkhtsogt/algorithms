class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        for i in range(1, len(nums)):
        	self.nums[i] += self.nums[i-1]
        	
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.nums[j] - (self.nums[i-1] if i > 0 else 0)


# Your NumArray object will be instantiated and called as such:
obj = NumArray([1, 2, 3, 4, 5, 6])
print obj.sumRange(0, 2)
print obj.sumRange(2, 5)
print obj.sumRange(0, 5)
