import random

DIMENSIONS = 2
MIN = -5.12
MAX = 5.12

def set_dimensions(dim):
	global DIMENSIONS
	DIMENSIONS = dim


def create_solution():
	
	return [random.uniform(MIN, MAX) for i in range(DIMENSIONS)]


def evaluate_solution(solution):
	sum = 0
	for index in range(DIMENSIONS-1):
		temp1 = (solution[index] * solution[index]) - solution[index+1]
		temp2 = solution[index] - 1.0
		sum += (100 * temp1 * temp1) + (temp2 * temp2)
	return sum
