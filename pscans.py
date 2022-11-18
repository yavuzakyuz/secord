from concurrent.futures import ThreadPoolExecutor
from socket import *


def scan_ports_of(host):
	ports=list(range(1, 65535))
	opened_ports = []
	def scanner(port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		try:
			connection = sock.connect((host, port))
			opened_ports.append(port)
			connection.close()
		except:
			pass
	with ThreadPoolExecutor(max_workers=5000) as pool:
		pool.map(scanner, ports)
	return(opened_ports)
