from stack import Stack
from octet2 import Octet
from copy import deepcopy
class Addres:

	default = '0.0.0.0' # tworzenie pustego adresu (nie wiem czy to ma sens, ale pasuje do konwencji)

	def __init__(self, addres = default):
		#self.addres = addres # reprezentacja tekstowa w 10-tnym
		self.octets = Addres.make_octets(addres) # lista oktetow (instancje Octet)
	
	def get_octet(self, number):
		assert number in (1, 2, 3, 4) , 'No octet with this number'
		return self.octets[number-1]

	def update_octet(self, new_octet, number):
		#print(type(new_octet))
		assert isinstance(new_octet, Octet) , 'Wrong type'
		assert number in (1, 2, 3, 4) , 'No octet with this number'
		self.octets[number-1] = new_octet
		return

	def __str__(self):
		str_rep ='.'.join(list(map(str, self.octets)))
		return str_rep

	def __iter__(self):
		return iter(self.octets) # iterowanie po adresie to iterowanie po liscie oktetow

	def __eq__(self, other):
		for k in (1,2,3,4):
			if self.get_octet(k) != other.get_octet(k):
				return False
		return True

	def increment(self):
		next_address = deepcopy(self)
		zero = Octet(0)
		for n in (4,3,2,1):
			old = next_address.get_octet(n)
			try:
				next_address.update_octet(old+Octet(1), n)
			except:
				next_address.update_octet(zero, n)
				continue
			break
		return next_address


	@staticmethod

	def make_octets(addres):
		octets=[]
		for number in addres.split('.'):
			octets.append(Octet(int(number)))
		return octets



class Mask(Addres): # maska podawana  w postaci prefiksowej
 	
 	def __init__(self, prefix):
 		addres = Mask.prefix_to_dec(prefix)
 		self.prefix = prefix
 		super().__init__(addres)

 	def __str__(self):
 		return '/'+str(self.prefix)+' '+super().__str__()
 	@staticmethod

 	def prefix_to_dec(prefix):
 		addres = []
 		while prefix >=8:
 			addres.append(255)
 			prefix-=8
 		if len(addres) < 4:
 			S=0
 			for k in range(7, 7-prefix, -1):
 				S+=2**k
 			addres.append(S)
 			while len(addres) < 4:
 				addres.append(0)
 		addres = '.'.join(list(map(str, addres)))
 		return addres

	

if __name__ == '__main__':
	pass
	
