class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None
	
	def add(self, x):
		listNode = ListNode(x)
		if self.first == None:
			self.first = listNode
			self.last = listNode
		else:
			self.last.next = listNode
			self.last = self.last.next
	
	def getFirst(self):
		return self.first
	
	def cout(self):
		node = self.first
		while node:
			print node.val	
			node = node.next
			
		

class Solution(object):
    def getIntersectionNode(self, headA, headB):
		"""
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		p, q = headA, headB
		data = {}
		while p:
			data[p] = 1
			p = p.next

		while q:
			if q in data:
				return q

			q = q.next

		return None

ll1 = LinkedList()
ll2 = LinkedList()
ll1.add(3)
ll2.add(2)
ll2.add(3)	
sol = Solution()
print sol.getIntersectionNode(ll1.getFirst(), ll2.getFirst())	
