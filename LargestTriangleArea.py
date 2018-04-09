class Solution(object):
    def largestTriangleArea(self, points):
		"""
		:type points: List[List[int]]
		:rtype: float
		"""
		def area(P, Q, R):
			#Shoelace formula
			return 0.5 * abs(P[0]*Q[1] + Q[0]*R[1] + R[0]*P[1]
				             -P[1]*Q[0] - Q[1]*R[0] - R[1]*P[0])
		size = len(points)
		largest = 0
		for i in range(0, size):
			for j in range(i+1, size):
				for k in range(j+1, size):
					largest = max(largest, area(points[i], points[j], points[k]))	

		return largest

		
        	
        
sol = Solution()
print sol.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
