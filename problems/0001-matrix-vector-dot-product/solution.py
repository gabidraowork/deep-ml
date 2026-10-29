def matrix_dot_vector(matrix: list[list[int|float]], vector: list[int|float]) -> list[int|float]:
	new_vector: list[int|float]= [0]*len(vector)
	
	try:
		for iy, line in enumerate(matrix):
			for ix,entry in enumerate(line):
				new_vector[iy] += entry*vector[ix]
	except:
		return -1
	
	return new_vector