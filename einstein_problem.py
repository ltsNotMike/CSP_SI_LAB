from problem import Problem
from itertools import permutations
from constraint import *
class EinsteinProblem(Problem):
	def __init__(self):
		super().__init__()
		domena_pali = ["Fajka", "Bez Filtra", "Mentol", "Cygaro", "Light"]
		domena_pije = ["Mleko", "Herbata", "Woda", "Kawa", "Piwo"]
		domena_kolor = ["Zielony", "Żółty", "Niebieski", "Biały", "Czerwony"]
		domena_zwierze = ["Konie", "Psy", "Ptaki", "Koty", "Rybki"]
		domena_narodowosc = ["Norweg", "Duńczyk", "Anglik", "Szwed", "Niemiec"]

		self.add_variable("Pali", permutations(domena_pali))
		self.add_variable("Pije", permutations(domena_pije))
		self.add_variable("Kolor", permutations(domena_kolor))
		self.add_variable("Zwierze", permutations(domena_zwierze))
		self.add_variable("Narodowość", permutations(domena_narodowosc))

		# Norweg mieszka w pierwszym domu
		self.add_constraint(FunctionConstraint(lambda narodowosc: narodowosc[0] == "Norweg"), ['Narodowość'])
		# Anglik mieszka w czerwonym domu
		self.add_constraint(FunctionConstraint(lambda narodowosc, kolor: narodowosc.index('Anglik') == kolor.index('Czerwony')), ['Narodowość', 'Kolor'])
		# Zielony dom znajduje się bezpośrednio po lewej stronie domu białego
		self.add_constraint(FunctionConstraint(lambda kolor: kolor.index('Zielony') + 1 == kolor.index('Biały')), ['Kolor'])
		# Duńczyk pija herbatkę
		self.add_constraint(FunctionConstraint(lambda narodowosc, pije: narodowosc.index('Duńczyk') == pije.index('Herbata')), ['Narodowość', "Pije"])
		# Palacz papierosów light mieszka obok hodowcy kotów
		self.add_constraint(FunctionConstraint(lambda zwierze, pali: abs(zwierze.index('Koty') - pali.index('Light') == 1)), ['Zwierze', "Pali"])
		# Mieszkaniec żółtego domu pali cygara
		self.add_constraint(FunctionConstraint(lambda kolor, pali: kolor.index("Żółty") == pali.index("Cygaro")), ['Kolor', "Pali"])
		# Niemiec pali fajkę
		self.add_constraint(FunctionConstraint(lambda narodowosc, pali: narodowosc.index("Niemiec") == pali.index("Fajka")), ['Narodowość', "Pali"])
		# Mieszkaniec środkowego domu pija mleko ( 0 1 2 3 4 )
		self.add_constraint(FunctionConstraint(lambda pije: pije.index("Mleko") == 2), ["Pije"])
		# Palacz papierosów light ma sąsiada, który pija wodę
		self.add_constraint(FunctionConstraint(lambda pije, pali: abs(pije.index('Woda') - pali.index('Light') == 1)), ["Pije", "Pali"])
		# Palacz papierosów bez filtra hoduje ptaki
		self.add_constraint(FunctionConstraint(lambda zwierze, pali: pali.index("Bez Filtra") == zwierze.index("Ptaki")), ["Zwierze", "Pali"])
		# Szwed hoduje psy
		self.add_constraint(FunctionConstraint(lambda zwierze, narodowosc: zwierze.index("Psy") == narodowosc.index("Szwed")), ["Zwierze", "Narodowość"])
		# Norweg mieszka obok niebieskiego domu
		self.add_constraint(FunctionConstraint(lambda kolor, narodowosc: abs(narodowosc.index('Norweg') - kolor.index('Niebieski') == 1)), ["Kolor", "Narodowość"])
		# Hodowca koni mieszka obok żółtego domu
		self.add_constraint(FunctionConstraint(lambda kolor, zwierze: abs(zwierze.index('Konie') - kolor.index('Żółty') == 1)), ["Kolor", "Zwierze"])
		# Palacz mentolowych pija piwo
		self.add_constraint(FunctionConstraint(lambda pali, pije: pali.index('Mentol') == pije.index('Piwo')), ["Pali", "Pije"])
		# W zielonym domu pija się kawę
		self.add_constraint(FunctionConstraint(lambda kolor, pije: kolor.index('Zielony') == pije.index('Kawa') ), ["Kolor", "Pije"])
		