from problem import Problem
from einstein_problem import EinsteinProblem
from map_problem import MapProblem
from variable import Variable
from constraint import *
def main():

	problem = MapProblem()
	
	problem.get_solution()
	# problem = EinsteinProblem()
	# problem.get_solution()

if __name__ == "__main__":
	main()

