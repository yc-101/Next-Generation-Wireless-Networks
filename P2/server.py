import socket
import cv2
import struct
import pickle

def server_program():
	host = "127.0.0.1"
	port = 5000

    # AF_INET: IPv4  ,  SOCK_STREAM: TCP (SOCK_DGRAM for UDP)
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.bind((host, port))
	server_socket.listen(1)

	print("=========================================")
	print(" - Waiting for connection...")
	print(" - Camera will open when a client joins.")
	print("=========================================")
	conn, address = server_socket.accept()
	print(" - Connection from: " + str(address))

	cap = cv2.VideoCapture(0)

	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
	
	welcome_msg =  "=========================================\n"
	welcome_msg += " - Connection successful!\n"
	welcome_msg += " - Command (in client's camera window):\n"
	welcome_msg += "	- ESC : exit\n"
	welcome_msg += "	- SPACE : screenshot\n"
	welcome_msg += "========================================="
	conn.sendall(welcome_msg.encode())

	while True:
		ret, frame = cap.read()
		result, encoded_frame = cv2.imencode('.jpg', frame, encode_param)
		data = pickle.dumps(encoded_frame, 0) # Serialize the encoded frame
		size = len(data)
		try:
			conn.sendall(struct.pack(">L", size) + data) # ">L" : unsigned long
		except:
			break

		cv2.imshow('Server', frame)
		key = cv2.waitKey(1) & 0xFF
		

	cap.release()
	cv2.destroyAllWindows()
	conn.close()

if __name__ == '__main__':
	server_program()