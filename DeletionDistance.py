'''
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string. For instance, the deletion distance between "heat" and "hit" is 3:
By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
We cannot get the same string from both strings by deleting 2 letters or fewer.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them. Explain how your function works, and analyze its time and space complexities.
'''
def deletion_distance(str1, str2):
	
	matrix = [[0] * (len(str1) + 2) for i in range(len(str2) + 2)]
	for i in range(len(str1) + 1):
		for j in range(len(str2) + 1):
			if i == 0:
				matrix[i][j] = j
			elif j == 0:
				matrix[i][j] = i
			elif str1[i - 1] == str2[j - 1]:
				matrix[i][j] = matrix[i - 1][j - 1]
			else:
				matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1])

	return matrix[len(str1)][len(str2)]		
	
print deletion_distance("heat", "hit")
