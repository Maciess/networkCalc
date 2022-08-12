from stack import Stack


class Binary:

	def __init__(self, integer = None):

		if integer is None:
			self.value10 = None
			self.value = []
		else:
			self.value10 = integer 
			self.value = Binary.convert(integer) #list 

	def decimal(self):
		return self.value10

	def get0b(self):
		return self.value

	def u0b(self, new_value):
		assert isinstance(new_value, list) and set(new_value) in ({0,1}, {0}, {1}, set()) , 'Wrong type'
		self.value = new_value
		self.value10 = Binary.deconvert(new_value)

	def udecimal(self, new_value):
		assert isinstance(new_value, int) and new_value >=0
		self.value10 = new_value
		self.value = Binary.convert(new_value)


	def __or__(self, other):
		assert isinstance(other, self.__class__) , 'Wrong type'
		num1  = self.get0b()
		num2  = other.get0b()
		d = len(num1) - len(num2)
		if d <= 0:
			num1 = [0 for k in range(abs(d))]+num1
		else:
			num2 = [0 for k in range(abs(d))]+num2
		new_value = [None for k in num1]
		for k in range(len(num1)):
			new_value[k] = num1[k] or num2[k]
		new = self.__class__()
		new.u0b(Binary.trim(new_value))
		return new

	def __and__(self, other):
		assert isinstance(other, self.__class__) , 'Wrong type'
		num1  = self.get0b()
		num2  = other.get0b()
		d = len(num1) - len(num2)
		if d <= 0:
			num1 = [0 for k in range(abs(d))]+num1
		else:
			num2 = [0 for k in range(abs(d))]+num2
		new_value = [None for k in num1]
		for k in range(len(num1)):
			new_value[k] = num1[k] and num2[k]
		new = self.__class__()
		new.u0b(Binary.trim(new_value))
		return new

	def __eq__(self, other):
		return self.get0b() == other.get0b()


	def __invert__(self):
		assert self.get0b is not [] , 'error'
		new = self.__class__() #wywolanie konstruktora
		new_value = self.get0b().copy()
		for i in range(len(new_value)):
			new_value[i] = int(not self.value[i])
		
		new.u0b(Binary.trim(new_value))
		return new

	def __add__(self, other):
		
		
		assert isinstance(other, self.__class__) , 'Wrong type'
		#Wyrownanie
		carry = 0
		num1  = self.get0b()
		num2  = other.get0b()
		d = len(num1) - len(num2)
		if d <= 0:
			num1 = [0 for k in range(abs(d))]+num1
		else:
			num2 = [0 for k in range(abs(d))]+num2
		new_value = [None for k in num1]
		for k in range(len(num1)-1,-1,-1):
			new_value[k] = num1[k] ^ num2[k] ^ carry
			carry = ((num1[k] & num2[k]) | (num1[k] & carry)) | (num2[k] & carry)
		new_value.insert(0, carry)
		new = self.__class__()
		new.u0b(Binary.trim(new_value))
		return new



			
	def __str__(self):
		if self.value == []: return '0'
		string_rep = ''
		for _ in self.value:
			string_rep +=str(_)
		return string_rep


	@staticmethod

	def convert(number):
		if number == 0:
			return [0]
		stack = Stack()
		result = []
		while number > 0:
			stack.push(number % 2)
			number = number // 2
		while not stack.is_empty():
			result.append(stack.pop())
		return result
	def deconvert(number_0b):
		number = 0
		length = len(number_0b)
		for k in range(length):
			number+=number_0b[k]*2**(length-1-k)
		return number

	def trim(table):
		if table is [] or table[0] == 1:
			return table
		elif 1 not in table:
			return [0]
		else:
			return table[table.index(1):]



if __name__ == '__main__':		
	pass