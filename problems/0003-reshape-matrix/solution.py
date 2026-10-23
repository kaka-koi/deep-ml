import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	row,col=new_shape
	mat=np.array(a)
	total_value=mat.size
	if total_value==row*col:
		reshaped_matrix=mat.reshape(new_shape)
	    return reshaped_matrix
	else:
		return []

	# reshaped_matrix=np.reshape(a,new_shape)
	# or
	# a=np.array(a)
	