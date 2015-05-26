import socket

def Main():
	host = '192.168.0.229'
	port = 5000

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print "Connection from: " + str(addr)
	while True:
		data = c.recv(1024)
		if not data:
			break
		print "From connected user: " + str(data)
		data = str(data).upper()
		print "Sending: " + str(data)
		c.send(data)
	c.close()

if __name__ == '__main__':
	Main()
