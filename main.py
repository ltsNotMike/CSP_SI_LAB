from problem import Problem
from einstein_problem import EinsteinProblem
from constraint import *
def main():

	problem = Problem()
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

	# problem = EinsteinProblem()
	# problem.get_solution()

if __name__ == "__main__":
	main()

