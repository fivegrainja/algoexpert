def isValidSubsequence(array, sequence):
	
	for i in sequence:
		try:
			pos = array.index(i)
		except ValueError:
			return False
		array = array[pos+1:]
	return True
	