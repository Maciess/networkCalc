from ip_v4 import Addres, Mask
from DHCP import DHCP
#header test

class Network:
	def __init__(self, ip_addres, mask): # w konstruktorze tekstowo
		
		self.mask = Mask(mask)
		self.network_addres = Network.make_network_address(ip_addres, self.mask)
		self.broadcast = Network.make_broadcast(self.network_addres, self.mask)
		self.DHCP = DHCP(self.network_addres, self.broadcast)
		self.hosts = self.DHCP.create_hosts()

	def __str__(self):
		return 'Adres sieci: {}\nMaska: {}\nBroadcast: {}\nPierwszy host: {}\nOstatni host: {}'.format(str(self.network_addres), str(self.mask), str(self.broadcast), str(self.get_first_host()), str(self.get_last_host()))

	def get_first_host(self):
		return self.hosts.get_head().get_data()

	def get_last_host(self):
		return self.hosts.get_tail().get_data()
	@staticmethod
	
	def make_broadcast(ip_addres, mask): # tutaj juz jako instancje Addres
		broadcast = Addres()
		for n in (1,2,3,4):
			network_octet = ip_addres.get_octet(n)
			mask_octet = mask.get_octet(n)
			broadcast_octet = network_octet.naive_mul(mask_octet)
			broadcast.update_octet(broadcast_octet, n)
		return broadcast

	def make_network_address(ip_addres, mask):
		net_addres = Addres()
		ip_addres = Addres(ip_addres)
		for n in (1,2,3,4):
			ip_octet = ip_addres.get_octet(n)
			mask_octet = mask.get_octet(n)
			net_octet = ip_octet & mask_octet
			net_addres.update_octet(net_octet, n)
		return net_addres

if __name__ == '__main__':
	pass