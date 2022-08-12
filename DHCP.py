from host import Host
from linked_list import *
class DHCP:
	
	def __init__(self, first_addres, last_addres):
		self.first_addres = first_addres
		self.last_addres = last_addres
	
	def create_hosts(self):
		List = LinkedList()
		tmp = self.first_addres.increment()
		while tmp != self.last_addres:
			List.push_back(Host(tmp))
			tmp = tmp.increment()
		return List