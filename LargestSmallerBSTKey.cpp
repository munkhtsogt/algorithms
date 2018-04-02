#include <iostream>
#include <algorithm>

using namespace std;

struct Node
{
	int key;
	Node *left;
	Node *right;
	Node *parent;
};

// Helper function that allocates a new Node 
Node* newNode( int key )
{
	Node* n = new Node;
	n->key = key;
	n->left = NULL;
	n->right = NULL;
	n->parent = NULL;

	return n;
}

//  Given a binary search tree and a number, inserts a new Node with
//  the given number in the correct place in the tree. Returns the new
//  root pointer which the caller should then use 
Node *insert( Node *root, int key )
{
	// 1) If the tree is empty, return a new single Node
	if( root == NULL )
  		return newNode( key );

	Node *temp;

	// 2) Otherwise, recur down the tree
	if( key < root->key )
	{
	  	temp = insert( root->left, key );
	  	root->left = temp;
	  	temp->parent = root;
	} 
	else
	{
	  	temp = insert( root->right, key );
	  	root->right = temp;
	  	temp->parent = root;
	}

	// Return the (unchanged) Node pointer
	return root;
}

int findLargestSmallerKey(Node *rootNode, int num) 
{
  	// your code goes here
  	Node * current = rootNode;
  	int result = -1;
  	while (current != NULL){
  		if(current -> key >= num){
  			current = current -> left;
  		}
  		else {
  			result = max(result, current->key);
  			current = current -> right;
  		}
  	}
  	return result;
}

int findLargestSmallerKey2(Node *rootNode, int num){
	if(rootNode -> left == NULL || rootNode -> right == NULL) return rootNode -> key;
	
	if(rootNode->key >= num)
		findLargestSmallerKey2(rootNode->left, num);
	else
		findLargestSmallerKey2(rootNode->right, num);
} 

int main() {
	Node * root = newNode(20);
	insert(root, 9);
	insert(root, 25);
	insert(root, 5);
	insert(root, 12);
	insert(root, 11);
	insert(root, 14);
	cout << findLargestSmallerKey2(root, 17) << endl;
	return 0;
}
