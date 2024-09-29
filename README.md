# 次世代無線網路概論 Introduction to Next-Generation Wireless Networks


## Project1 - WireShark
- Wireshark sniffing
- Python program to send a packet to URL


## Project2 - TCP socket programming
- This project aims to implement an application for transmitting real-time video streaming between the client and the server.
- A camera positioned on the server captures real-time images. Once the server reads the live image, it is showcased on the screen and transmitted to the client.
- The client receives the video stream from the server and displays it on the screen. Additionally, the client needs to provide the screenshot function.

### Server (only one server)
1. Construct a TCP connection with the connected client.
2. Open a TCP socket.
3. Wait for the client.
4. Read live video from the camera and display it on the screen.
5. Transmit the live video to the client.
6. Close the TCP connection when the client finishes the task.

### Client (only one client)
1. Build a TCP connection with its target server.
2. Open a TCP socket.
3. Connect to the server.
4. Receive live video from the server and display it.
5. If the client presses the “space” key, it will take a screenshot and save it on disks.
6. Finish the TCP connection(ctrl+c or “ESC” key).
