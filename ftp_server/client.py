import socket

class Exit(Exception):
	pass

sock = socket.socket()
server = input('Enter IP address: ')  # 'localhost'
port = input('Enter port: ')  # 9090
print()

try:
	# connect to server
	sock.connect((server, int(port)))

	# server
	print(f"Server IP: {server}; Port: {port}")

	# client
	host = sock.getsockname()
	print(f"Client IP: {host[0]}; Port: {host[1]}")

except ConnectionRefusedError as c:
	print(f"ERROR {c}")
	exit()


while True:

	try:
		data = sock.recv(1024).decode("utf8")

		# disconnect from server
		if len(data) == 0 or data.lower() == 'stop' or data.lower() == 'exit':
			raise Exception("You disconnected.")

		# exceptions
	except ConnectionResetError as e:
		print(f"ERROR: {e}")
		sock.close()
		exit()

	except Exception as s:
		print(f"ERROR: {s}")
		sock.close()
		exit()

	print(f"\nServer: {data}")


	try:
		promt = input("\nYou: ")
	except KeyboardInterrupt as k:
		print(f"ERROR: {k}")
		exit()

	try:
		result = sock.send(promt.encode())
		if not result:
			raise Exception("Date not found")
	except Exception as e:
		print(f"ERROR: {e}")
		exit()


sock.close()
