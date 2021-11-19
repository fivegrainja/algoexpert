from pprint import  pprint

def apartmentHunting(blocks, reqs):
	# Each element in scores represents a block. Each element has an entry for each amentity type in reqs. The value of
	# these is the distance from that block to the nearest amenity of that type.
	
	# For each req type
	# - build list of the locations of this req type
	# - add scores for this req type to scores

	scores = [{} for i in range(len(blocks))]
	
	for r in reqs:
		locations = []
		for i, b in enumerate(blocks):
			if b[r]:
				locations.append(i)
		nearest_left_index = None
		nearest_right_index = 0
		for i, b in enumerate(blocks):
			# Update nearest_left_index and nearest_right_index if necessary
			if b[r]:
				if nearest_left_index is None:
					nearest_left_index = 0
				else:
					nearest_left_index += 1
				nearest_right_index += 1
				if nearest_right_index == len(locations):
					nearest_right_index = None
			# Calculate scores for this block for r
			if nearest_left_index is None:
				distance_left = None
			else:
				distance_left = i - locations[nearest_left_index]
			if nearest_right_index is None:
				distance_right = None
			else:
				distance_right = locations[nearest_right_index] - i
			if distance_left is None:
				scores[i][r] = distance_right
			elif distance_right is None:
				scores[i][r] = distance_left
			else:
				scores[i][r] = min(distance_left, distance_right)

	pprint(blocks)
	pprint(scorets)
	
	shortest_longest_distance = len(blocks)
	shortest_longest_block = -1
	for i, s in enumerate(scores):
		this_longest_distance = max(s.values())
		print(f'block {i} longest distance {this_longest_distance}')
		if this_longest_distance < shortest_longest_distance:
			shortest_longest_distance = this_longest_distance
			shortest_longest_block = i
	print(f'{shortest_longest_distance=} {shortest_longest_block=}')
	return shortest_longest_block
	
				