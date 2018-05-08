class Solution(object):
    def subdomainVisits(self, cpdomains):
		"""
		:type cpdomains: List[str]
		:rtype: List[str]
		"""
		domain = {}
		for d in cpdomains:
			d = d.split(' ')
			if d[1] not in domain:
				domain[d[1]] = int(d[0])
			else:
				domain[d[1]] += int(d[0])
	
			subs = d[1].split('.')
			for j in range(1, len(subs)):
				sub = '.'.join(subs[j:])
				if sub not in domain:	
					domain[sub] = int(d[0])
				else:
					domain[sub] += int(d[0])
		r = []
		for k in domain:
			r.append(str(domain[k]) + " " + k)
			
					
		return r
			
print Solution().subdomainVisits(["9001 discuss.leetcode.com"])        
print Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])

