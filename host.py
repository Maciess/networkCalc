from ip_v4 import Addres

class Host:

	def __init__(self, addres):
		assert isinstance(addres, Addres) , 'Wrong addres type'
		self.ip  = addres #
		#self.mac = 'mac addres'

	def __str__(self):
		return str(self.ip)


if __name__ == '__main__':
	pass