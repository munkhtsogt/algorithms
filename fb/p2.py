def isPalindrome(st):
	l, r = 0, len(st) - 1
	while l <= r:
		if st[l] == st[r]:
			r -= 1
			l += 1
		else:
			return False
	
	return True

		
