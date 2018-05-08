class Solution(object):
    def countBattleships(self, board):
		"""
		:type board: List[List[str]]
		:rtype: int
		"""
		count = 0
		for i in xrange(len(board)):
			for j in xrange(0, len(board[i])):
				c = 1
				if board[i][j] == "X":
					if i > 0 and board[i - 1][j] != '.': c = 0
					if j > 0 and board[i][j - 1] != '.': c = 0
					count += c

		return count

board = [['X', '.', '.', 'X'], 
		 ['.', '.', '.', 'X'], 
		 ['.', '.', '.', 'X']]
print Solution().countBattleships([[".","."],["X","X"]]) 
        
