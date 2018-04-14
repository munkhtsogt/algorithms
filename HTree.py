import math
'''
TIME COMPLEXITY: 1 + 4 + 4 ^ 2 + ... 4 ^ (n - 1) = O(4^n)
SPACE COMPLEXITY: O(1)
'''
class Solution(object):
	
	def drawHTree(self, x, y, length, depth):
		'''
		center X, Y, length, depth
		'''
		if depth == 0:
			return
		
		# DRAW A HTREE	
		half = length / 2
		leftEnd = x - half
		rightEnd = x + half
		
		topY = y + half
		bottomY = y - half
		
		self.drawLine(leftEnd, y, rightEnd, y)
		self.drawLine(leftEnd, topY, leftEnd, bottomY)
		self.drawLine(rightEnd, topY, rightEnd, bottomY)
		
		nextLength = length / math.sqrt(2)	
		depth -= 1
		self.drawHTree(leftEnd, topY, nextLength, depth)
		self.drawHTree(rightEnd, topY, nextLength, depth)
		self.drawHTree(leftEnd, bottomY, nextLength, depth)
		self.drawHTree(rightEnd, bottomY, nextLength, depth)		
		
	def drawLine(self, x1, y1, x2, y2):
		'''
		DRAW A LINE BETWEEN GIVEN COORDINATES
		'''
		print x1, y1, x2, y2





Solution().drawHTree(8, 0, 16, 3)
