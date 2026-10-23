def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0])!=len(b):
		return -1
	
	result=[]

    for matrix_i in a:
		vector_index=0
		dot_value=0
		while vector_index<len(b):
			dot_value+=matrix_i[vector_index]*b[vector_index]
			vector_index+=1
		result.append(dot_value)
	
	return result
		

	


	