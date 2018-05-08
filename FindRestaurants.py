class Solution(object):
    def findRestaurant(self, list1, list2):
		"""
		:type list1: List[str]
		:type list2: List[str]
		:rtype: List[str]
		"""
		r, res2 = {}, {}
		
		for i, e in enumerate(list2):
			res2[e] = i
		
		for i, e in enumerate(list1):
			if e in res2:
				r[e] = i + res2[e]	
		
		r = sorted(r.items(), key=lambda x: x[1])
		freq = r[0][1]
		result = [r[0][0]]
		for i in range(1, len(r)):
			if freq == r[i][1]:
				result.append(r[i][0])
			else:
				break
					
		return result
        
res1 = ["Shogun", "Tapioca Express", "Burger King", "Piatti"]
res2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]        
print Solution().findRestaurant(res1, res2)
