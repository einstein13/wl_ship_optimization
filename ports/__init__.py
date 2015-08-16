from settings import PORTS

for port in PORTS:
	__import__('ports.'+port)