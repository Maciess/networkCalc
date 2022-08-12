from binary import Binary
from copy import deepcopy
# inne podejscie do Octet
# klasa Binary o okreslonej dlugosci 
class Octet(Binary):

	def __init__(self, integer = None):
		assert integer in range(256) or integer is None ,  'Out or range'
		super().__init__(integer)
		self.u0b(Octet.complete(self.get0b()))



	def naive_mul(self, other):
		# implikacja wiec nie mozna uzyc ladnego operatora :(
		result = self | ~other
		return result

	def __or__(self, other):
		result = super().__or__(other)
		result.u0b(Octet.complete(result.get0b()))
		return result

	def __and__(self, other):
		result = super().__and__(other)
		result.u0b(Octet.complete(result.get0b()))
		return result

	def __invert__(self):
		result = super().__invert__()
		result.u0b(Octet.complete(result.get0b()))
		return result

	def u0b(self, new_value):
		assert len(new_value) <= 8 , 'Octet limit is 255'
		super().u0b(Octet.complete(new_value))

	def udecimal(self, new_value):
		assert new_value in range(256) , 'Octet limit is 255'
		super().udecimal(new_value)




	@staticmethod

	def complete(table):
		if table != []:
			d = len(table)
			buff = [0 for k in range(8-d)]
			table = buff+table
		return table


	



if __name__ == '__main__':
	pass
