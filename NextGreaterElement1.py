class Solution(object):
	def nextGreaterElement(self, findNums, nums):
		d = {}
		st = []
		result = []

		for x in nums:
			while len(st) and st[-1] < x:
				d[st.pop()] = x
			st.append(x)

		for x in findNums:
			result.append(d.get(x, -1))

		return result
		
sol = Solution()
num1 = [4, 1, 2]
num2 = [1, 3, 4, 2]
print sol.nextGreaterElement(num1, num2)

