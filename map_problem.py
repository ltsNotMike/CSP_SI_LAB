from problem import Problem
from constraint import AllDifferentConstraint

class MapProblem(Problem):
	def __init__(self):
		# TODO: Auto generate the map
		super().__init__()
		self.add_variable('1', ['R', 'G', 'B'])
		self.add_variable('2', ['R', 'G', 'B'])
		self.add_variable('3', ['R', 'G', 'B'])
		self.add_variable('4', ['R', 'G', 'B'])
		self.add_variable('5', ['R', 'G', 'B'])
		self.add_variable('6', ['R', 'G', 'B'])
		self.add_variable('7', ['R', 'G', 'B'])
		self.add_variable('8', ['R', 'G', 'B'])
		self.add_variable('9', ['R', 'G', 'B'])
		self.add_variable('0', ['R', 'G', 'B'])

		self.add_constraint(AllDifferentConstraint(), ['1', '2'])
		self.add_constraint(AllDifferentConstraint(), ['1', '5'])
		self.add_constraint(AllDifferentConstraint(), ['2', '3'])
		self.add_constraint(AllDifferentConstraint(), ['2', '5'])
		self.add_constraint(AllDifferentConstraint(), ['2', '6'])
		self.add_constraint(AllDifferentConstraint(), ['2', '7'])
		self.add_constraint(AllDifferentConstraint(), ['3', '7'])
		self.add_constraint(AllDifferentConstraint(), ['4', '7'])
		self.add_constraint(AllDifferentConstraint(), ['4', '8'])
		self.add_constraint(AllDifferentConstraint(), ['6', '9'])
		self.add_constraint(AllDifferentConstraint(), ['7', '8'])
		self.add_constraint(AllDifferentConstraint(), ['7', '9'])
		self.add_constraint(AllDifferentConstraint(), ['8', '0'])
		self.add_constraint(AllDifferentConstraint(), ['9', '0'])