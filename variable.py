import copy

class Variable:
	def __init__(self, name: str, domain: list):
		self.name = name
		self.domain = copy.deepcopy(domain)
		self.value = None
		self.domain_history = []

	@property
	def is_selected(self) -> bool:
		""" Returns true if the decision about the value of this variable has been selected """
		if __is_selected:
			return True
		elif len(self.domain) == 1:
			self.__is_selected = True
			self.__selected_index = 0
		return self.__is_selected
	
	def __repr__(self):
		return f"Variable({self.name}, {self.value})"

	def push_domain(self):
		self.domain_history.append(copy.deepcopy(self.domain))
		
	def pop_domain(self):
		self.domain = self.domain_history.pop()