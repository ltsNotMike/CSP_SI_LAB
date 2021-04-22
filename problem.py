from constraint import BaseConstraint
import copy
from variable import Variable
class Problem:
	def __init__(self):
		self.constraints = []
		self.variables = {}
	
	def add_constraint(self, constraint: BaseConstraint, variables: list) -> None:
		self.constraints.append((constraint, variables))

	def add_variable(self, name: str, domain: list) -> None:
		if name in self.variables:
			print("Problem: Tried to add the same variable twice")
		self.variables[name] = Variable(name, domain)

	def get_solution(self) -> map:
		self.backtracking([copy.deepcopy(x) for x in self.variables])
		# TODO: This assumes that it is always solved
		print(self.variables)
		return self.variables

	def backtracking(self, unassigned: list) -> None:
		print(unassigned)
		if len(unassigned) == 0:
			return
		variable = self.variables[unassigned[0]]
		for potential_value in variable.domain:
			if self.is_solved():
				return
			variable.value = potential_value
			if self.is_satisfying_constraints():
				self.backtracking(unassigned[1:])
			else:
				variable.value = None
	
	def forward_checking(self, unassigned: list) -> None:
		if len(unassigned) == 0:
			return
		
		# Select variable
		variable = self.variables[unassigned[0]]

		# State push
		for some_var in unassigned:
			if some_var != variable:
				self.variables[some_var].push_domain()
		
		# For each value in domain
		for potential_value in variable.domain:
			if self.is_solved():
				return

			# Select value for the variable and remove this value from domains of connected nodes
			variable.value = potential_value
			self.forward_check(variable.name, unassigned)

			if self.is_satisfying_constraints():
				self.forward_checking(unassigned[1:])
			else:
				variable.value = None
		
		for some_var in unassigned:
			if some_var != variable:
				self.variables[some_var].pop_domain()
	def forward_check(self, variable_name: str, unassigned: list):
		# For each constraint in the problem
		for constraint, variables in self.constraints:
			# Check if this constraint is connected with this variable
			# This could be for all constraints
			# However i think that this condition make it faster
			if variable_name in variables:
				# For each variable that is connected with this constraint ...
				for connected_variable_name in variables:
					# ... but is not the provided variable and is not yet assigned
					if connected_variable_name != variable_name and connected_variable_name in unassigned:
						# For each value in the domain
						for value in self.variables[connected_variable_name].domain:
							# Check if the value breaks the constraint
							self.variables[connected_variable_name].value = value
							if not constraint.is_satisfied([self.variables[name] for name in variables]):
								# Remove the value from domain ...
								self.variables[connected_variable_name].domain.remove(value)
						self.variables[connected_variable_name].value = None;

	def is_solved(self):
		for name in self.variables:
			if self.variables[name].value == None:
				return False
		return self.is_satisfying_constraints()

	def is_satisfying_constraints(self):
		for constraint, variables in self.constraints:
			if not constraint.is_satisfied([self.variables[name] for name in variables]):
				return False
		return True