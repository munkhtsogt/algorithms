##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 71 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################


# A node 
class Node:

# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None

# A binary search tree 
class BinarySearchTree:

	# Constructor to create a new BST
	def __init__(self):
		self.root = None

	def helper(self, root, largest, num):
		if root != None:
			if root.key <= num:
				largest = max(largest, root.key)
			m1 = self.helper(root.left, largest, num)
			m2 = self.helper(root.right, largest, num)
			return max(largest, m1, m2)
			
	def find_largest_smaller_key(self, num):
		largest = -1
		return self.helper(self.root, largest, num)
	
	def findLargestSmallerKey(self, num):
		largest = -1
		currentNode = self.root
		while currentNode != None:
	  		if currentNode.key < num:
				largest = max(currentNode.key, largest)
				currentNode = currentNode.right
		  	else:
				currentNode = currentNode.left
		return largest
	# Given a binary search tree and a number, inserts a
	# new node with the given number in the correct place
	# in the tree. Returns the new root pointer which the
	# caller should then use(the standard trick to avoid
	# using reference parameters)
	def insert(self, key):

	  	# 1) If tree is empty, create the root
		if (self.root is None):
	  		self.root = Node(key)
		  	return

		# 2) Otherwise, create a node with the key
		#    and traverse down the tree to find where to
		#    to insert the new node
		currentNode = self.root
		newNode = Node(key)

		while(currentNode is not None):
			if(key < currentNode.key):
		  		if(currentNode.left is None):
					currentNode.left = newNode
					newNode.parent = currentNode
					break
			  	else:
					currentNode = currentNode.left
			else:
		  		if(currentNode.right is None):
					currentNode.right = newNode
					newNode.parent = currentNode
					break
		  		else:
					currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################

bst  = BinarySearchTree()
 
# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9);
bst.insert(25);
bst.insert(5);
bst.insert(12);
bst.insert(11);  
bst.insert(14);    

result = bst.find_largest_smaller_key(17)

print "Largest smaller number is ", result

