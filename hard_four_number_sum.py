from itertools import combinations
from pprint import pprint

def fourNumberSum(array, targetSum):
	print(f'{array=}')
    quads = []
    for p in combinations(array, 4):
		print(f'{p=}')
		if sum(p) == targetSum:
			print(f'sum of {p} is {sum(p)}')
			quads.append(p)
	return quads
