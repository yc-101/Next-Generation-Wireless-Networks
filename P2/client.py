import socket
import cv2
import struct
import pickle

def client_program():
    host = "127.0.0.1"
    port = 5000

    # AF_INET: IPv4  ,  SOCK_STREAM: TCP (SOCK_DGRAM for UDP)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    client_socket.connect((host, port))

    data = b""
    payload_size = struct.calcsize(">L") # ">L" :　unsigned long

    welcome_msg = client_socket.recv(1024).decode()
    print(welcome_msg)

    while True:
        while len(data) < payload_size:
            data += client_socket.recv(4096)

        packed_msg_size = data[:payload_size]   # 把位置 0~payload_size 打包
        data = data[payload_size:]              # 把位置 0~payload_size 刪除

        msg_size = struct.unpack(">L", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4096)

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        cv2.imshow('Client', frame)
        key = cv2.waitKey(1) & 0xFF # 每1毫秒檢查一次

        # Command
        if key == ord(' '): # SPACE
            print("Screenshot taken")
            cv2.imwrite('screenshot_1.jpg', frame)
        elif key == 27: # ESC
            print("Quit")
            break

    client_socket.close()

if __name__ == '__main__':
    client_program()