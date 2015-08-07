class CallingShip():
	ships_to_call = 0

	def number_ships_to_call(self):
		return self.ships_to_call

	def is_port_calling(self):
		return self.ships_to_call > 0

	def set_ships_to_call(self, number):
		self.ships_to_call = number
		return number

	def copy_CallingShip(self, destination_port):
		destination_port.ship_to_call = self.ships_to_call
		return destination_port
