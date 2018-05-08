def differenceK(nums, k):
	diff = {}
	for i in range(0, len(nums)):
		diff[nums[i]] = i

	result = []
	for i in range(0, len(nums)):
		x = nums[i] - k
		y = nums[i] + k
		if x in diff:
			pair = (i, diff[x]) if i < diff[x] else (diff[x], i)
			if pair not in result:
				result.append(pair)
		elif y in diff:
			pair = (i, diff[y]) if i < diff[y] else (diff[y], i)
			if pair not in result:
				result.append(pair)	 
	
	return result

print differenceK([1, 7, 5, 9, 2, 12, 3], 2)
