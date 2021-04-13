from typing import Callable
class BaseConstraint:
	def is_satisfied(self, variables: list) -> bool:
		""" Returns true if the constraint is satisfied """
		pass
	
class FunctionConstraint(BaseConstraint):
	def __init__(self, function: Callable):
		self.__function = function

	def is_satisfied(self, variables: list) -> bool:
		values = [v.value for v in variables]
		if None in values:
			return True
		return self.__function(*values)

class EqualConstraint(BaseConstraint):
	def is_satisfied(self, variables: list) -> bool:
		for variable in variables:
			if variable.value != variables[0].value:
				return False
		return True

class AllDifferentConstraint(BaseConstraint):
	def __init__(self):
	 	super().__init__()
	""" Check if all values of variables are different """	
	def is_satisfied(self, variables):
		vars_seen = {}
		for variable in variables:
			# If the variable is assigned
			if variable.value != None:
				if variable.value in vars_seen:
					return False
				else:
					vars_seen[variable.value] = True
		return True