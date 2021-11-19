from itertools import combinations

def twoNumberSum(array, targetSum):
	pair = []
	for p in combinations(array, 2):
		if sum(p) == targetSum:
			pair = p
			break
	return pair
