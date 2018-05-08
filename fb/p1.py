def isCheck(words, ordering):
	i, j = 0, 0
	while i < len(words) and j < len(ordering):
		k, l = 0, 0
		while k < len(words[i]) and l < len(ordering):
			if words[i][k] == ordering[l]:
				k += 1
			else:
				l += 1
				
		if k != len(words[i]): return False
		
		if words[i][0] == ordering[j]:
			i += 1
		else:
			j += 1

	return True if i == len(words) else False 


print isCheck(['cc', 'cb', 'bb', 'ac'], ['c', 'b', 'a'])
#print filter(lambda x: x.isdigit(), "ab123c4")
