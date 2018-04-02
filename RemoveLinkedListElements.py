# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.first = None
		self.last = None

	def add(self, x):
		node = ListNode(x)
		if self.first == None:
			self.first = node
			self.last = node
		else:
			self.last.next = node
			self.last = self.last.next
	
	def getHead(self):
		return self.first	
		
	def cout(self):
		node = self.first
		while node:
			print node.val
			node = node.next
	
	def coutByHead(self, head):
		while head:
			print head.val
			head = head.next
	

class Solution(object):
    def removeElements(self, head, val):
		"""
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		current = head
		while current.next:
			if current.next.val == val:
				current.next = current.next.next
			else:
				current = current.next
	
		return head.next if head.val == val else head
        
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(2)
ll.add(1)
#ll.cout()
sol = Solution()
ll.coutByHead(sol.removeElements(ll.getHead(), 2))
