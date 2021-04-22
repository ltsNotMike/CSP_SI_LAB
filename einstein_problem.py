from problem import Problem
from itertools import permutations
from constraint import *
class EinsteinProblem(Problem):
	def __init__(self):
		super().__init__()
		domain_smokes = ["Pipe", "Unfiltered", "Menthol", "Cigar", "Light"]
		domain_drinks = ["Milk", "Tea", "Water", "Coffee", "Beer"]
		domain_color = ["Green", "Yellow", "Blue", "White", "Red"]
		domain_pet = ["Horse", "Dog", "Bird", "Cat", "Fish"]
		domain_nationality = ["Norwegian", "German", "Brit", "Swede", "Dane"]

		self.add_variable("Smokes", list(permutations(domain_smokes)))
		self.add_variable("Drinks", list(permutations(domain_drinks)))
		self.add_variable("Color", list(permutations(domain_color)))
		self.add_variable("Pet", list(permutations(domain_pet)))
		self.add_variable("Nationality", list(permutations(domain_nationality)))

		# Norweg mieszka w pierwszym domu
		self.add_constraint(FunctionConstraint(lambda nationality: nationality[0] == "Norwegian"), ['Nationality'])
		# Anglik mieszka w czerwonym domu
		self.add_constraint(FunctionConstraint(lambda nationality, color: nationality.index('Brit') == color.index('Czerwony')), ['Nationality', 'Color'])
		# Zielony dom znajduje się bezpośrednio po lewej stronie domu białego
		self.add_constraint(FunctionConstraint(lambda color: color.index('Green') + 1 == color.index('Biały')), ['Color'])
		# Duńczyk pija herbatkę
		self.add_constraint(FunctionConstraint(lambda nationality, drinks: nationality.index('Dane') == drinks.index('Tea')), ['Nationality', "Drinks"])
		# Palacz papierosów light mieszka obok hodowcy kotów
		self.add_constraint(FunctionConstraint(lambda pet, smokes: abs(pet.index('Cat') - smokes.index('Light')) == 1), ['Pet', "Smokes"])
		# Mieszkaniec żółtego domu smokes cygara
		self.add_constraint(FunctionConstraint(lambda color, smokes: color.index("Yellow") == smokes.index("Cigar")), ['Color', "Smokes"])
		# Niemiec smokes fajkę
		self.add_constraint(FunctionConstraint(lambda nationality, smokes: nationality.index("German") == smokes.index("Pipe")), ['Nationality', "Smokes"])
		# Mieszkaniec środkowego domu pija mleko ( 0 1 2 3 4 )
		self.add_constraint(FunctionConstraint(lambda drinks: drinks.index("Milk") == 2), ["Drinks"])
		# Palacz papierosów light ma sąsiada, który pija wodę
		self.add_constraint(FunctionConstraint(lambda drinks, smokes: abs(drinks.index('Water') - smokes.index('Light')) == 1), ["Drinks", "Smokes"])
		# Palacz papierosów bez filtra hoduje ptaki
		self.add_constraint(FunctionConstraint(lambda pet, smokes: smokes.index("Unfiltered") == pet.index("Bird")), ["Pet", "Smokes"])
		# Szwed hoduje psy
		self.add_constraint(FunctionConstraint(lambda pet, nationality: pet.index("Dog") == nationality.index("Swede")), ["Pet", "Nationality"])
		# Norweg mieszka obok niebieskiego domu
		self.add_constraint(FunctionConstraint(lambda color, nationality: abs(nationality.index('Norwegian') - color.index('Blue')) == 1), ["Color", "Nationality"])
		# Hodowca koni mieszka obok żółtego domu
		self.add_constraint(FunctionConstraint(lambda color, pet: abs(pet.index('Horse') - color.index('Yellow')) == 1), ["Color", "Pet"])
		# Palacz mentolowych pija piwo
		self.add_constraint(FunctionConstraint(lambda smokes, drinks: smokes.index('Menthol') == drinks.index('Beer')), ["Smokes", "Drinks"])
		# W zielonym domu pija się kawę
		self.add_constraint(FunctionConstraint(lambda color, drinks: color.index('Green') == drinks.index('Kawa') ), ["Color", "Drinks"])
		