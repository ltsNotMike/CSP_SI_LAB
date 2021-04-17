from problem import Problem
from einstein_problem import EinsteinProblem
from variable import Variable
from constraint import *
def main():

	problem = Problem()
	problem.add_variable('1', ['R', 'G', 'B'])
	problem.add_variable('2', ['R', 'G', 'B'])
	problem.add_variable('3', ['R', 'G', 'B'])
	problem.add_variable('4', ['R', 'G', 'B'])
	problem.add_variable('5', ['R', 'G', 'B'])
	problem.add_variable('6', ['R', 'G', 'B'])
	problem.add_variable('7', ['R', 'G', 'B'])
	problem.add_variable('8', ['R', 'G', 'B'])
	problem.add_variable('9', ['R', 'G', 'B'])
	problem.add_variable('0', ['R', 'G', 'B'])

	problem.add_constraint(AllDifferentConstraint(), ['1', '2'])
	problem.add_constraint(AllDifferentConstraint(), ['1', '5'])
	problem.add_constraint(AllDifferentConstraint(), ['2', '3'])
	problem.add_constraint(AllDifferentConstraint(), ['2', '5'])
	problem.add_constraint(AllDifferentConstraint(), ['2', '6'])
	problem.add_constraint(AllDifferentConstraint(), ['2', '7'])
	problem.add_constraint(AllDifferentConstraint(), ['3', '7'])
	problem.add_constraint(AllDifferentConstraint(), ['4', '7'])
	problem.add_constraint(AllDifferentConstraint(), ['4', '8'])
	problem.add_constraint(AllDifferentConstraint(), ['6', '9'])
	problem.add_constraint(AllDifferentConstraint(), ['7', '8'])
	problem.add_constraint(AllDifferentConstraint(), ['7', '9'])
	problem.add_constraint(AllDifferentConstraint(), ['8', '0'])
	problem.add_constraint(AllDifferentConstraint(), ['9', '0'])

	problem.get_solution()
	# problem = EinsteinProblem()
	# problem.get_solution()

if __name__ == "__main__":
	main()

