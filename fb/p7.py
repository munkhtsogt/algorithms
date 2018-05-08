def union(arr1, arr2):
	i, j = 0, 0
	r = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			r.append(arr1[i])
			i += 1
		elif arr1[i] > arr2[j]:
			r.append(arr2[j])
			j += 1
		else:
			r.append(arr1[i])
			i += 1
			j += 1
			
	while i < len(arr1):
		r.append(arr1[i])
		i += 1
		
	while j < len(arr2):
		r.append(arr2[j])
		j += 1	
	
	return r
	
def intersection(arr1, arr2):
	i, j = 0, 0
	r = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			i += 1
		elif arr1[i] > arr2[j]:
			j += 1
		else:
			r.append(arr1[i])
			j += 1
			i += 1
	return r
	
print union([1, 3, 4, 5, 7], [2, 3, 5, 6])
print intersection([1, 3, 4, 5, 7], [2, 3, 5, 6])
