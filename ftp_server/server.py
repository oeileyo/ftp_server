import socket
import datetime
from system import System


def save_log(text):
	log = open("logs.txt", "a")  # server logs

	now = datetime.datetime.now()
	log.write('<<' + str(now) + '>> ' + text + '\n')

	log.close()


system = System("")

# starting server
sock = socket.socket()
print('Server is starting.')
save_log('Server is starting.')


port = input('Enter port: ')
sock.bind(('', int(port)))


while True:

	# listening to the port
	sock.listen(1)
	print(f"Listening to the port ({port})")
	save_log(f"Listening to the port ({port})")


	# client address
	try:
		conn, addr = sock.accept()
	except KeyboardInterrupt as k:
		print(f"ERROR: {k}")
		save_log(f"ERROR: {k}")
		exit()

	print(f"Connected to {addr}")
	save_log(f"Connected to {addr[0]}:{addr[1]}")
	print()
	message = "Enter your home directory"
	conn.send(message.encode())
	print(f"Sending data: {message}")


	while True: # receiving client's message
		try:
			message = ""
			data = conn.recv(1024).decode("utf8")

		except ConnectionResetError as e:
			print(f"ERROR: {e}")
			save_log(f"ERROR: {e}")
			exit()

		except KeyboardInterrupt as k:
			print(f"ERROR: {k}")
			save_log(f"ERROR: {k}")
			exit()

		# clients commands
		if data == "" or data == "exit":
			print(f"Client disconnected")
			save_log(f"Client disconnected")
			break

		elif data == "stop":
			break

		elif system.way != "":
			message = system.main(data)

		# client enter root folder
		if system.way == "":
			message = system.setWay(data)
			save_log(message)

		print(f"Accepting data: {data}\n")
		save_log(f"Accepting data: {data}")

		# sending data back
		conn.send(message.encode())
		print(f"Sending data: {message}")
		save_log(f"Sending data: {message}")

	if data == "stop":
		break

print('Closing connection.')
save_log('Closing connection.')
conn.close()
