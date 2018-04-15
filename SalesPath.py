import sys

def get_cheapest_cost(rootNode):

	if len(rootNode.children) == 0:
	  return rootNode.cost

	minCost = sys.maxint
	for child in root.children:
		minCost = min(minCost, get_cheapest_cost(child))      

	return minCost + rootNode.cost
