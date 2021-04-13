from problem import Problem
from variable import Variable
from constraint import *
def main():
	# DEBUG: This should be generated
	some_map = {
		1: [3, 4, 5, 6],
		2: [4, 5],
		3: [1, 4, 6],
		4: [1, 2, 3],
		5: [1, 2],
		6: [1, 3]
	}
	
	problem = Problem()
	# Państwa i ich kolory
	problem.add_variable("T", [i for i in range(1,10)])
	problem.add_variable("O", [i for i in range(10)])
	problem.add_variable("F", [i for i in range(1,10)])
	problem.add_variable("W", [i for i in range(10)])
	problem.add_variable("R", [i for i in range(10)])
	problem.add_variable("U", [i for i in range(10)])
	# Granice
	def sum_function(t, w, o, f, u, r):
		is_sat = 2 * (t * 100 + w * 10 + o) == f * 1000 + o * 100 + u * 10 + r
		if is_sat:
			print(f"TWO = {t}{w}{o}; FOUR = {f}{o}{u}{r}")
		return is_sat
		
	problem.add_constraint(FunctionConstraint(sum_function), ['T', 'W', 'O', 'F', 'U', 'R'])
	problem.add_constraint(AllDifferentConstraint(), ['T', 'W', 'O', 'F', 'U', 'R'])
	

	problem.get_solution()

if __name__ == "__main__":
	main()

