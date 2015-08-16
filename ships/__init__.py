from settings import SHIPS

for ship in SHIPS:
	__import__('ships.'+ship)