from _thread import * 
import socket
import sys
from pathlib import Path

#The Writing thread function
def writing_function():
    #Take Port Number of Reading Thread as input 
    port = int(input("Enter the port number to which you want to connect: "))
    writing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Connect to the reading port
    writing_socket.connect(("localhost",port))

    while True:
        #take message as input
        msg = input()

        #File Transfer
        if msg.startswith("transfer "):
            filename = msg.split(" ")[1]
            path = Path(f"{filename}")
            if(path.is_file()):
                writing_socket.sendall(msg.encode())
                print("Sending the file...")
    
                with open(filename,"rb") as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        writing_socket.send(data)
                        if len(data) < 1024:
                            break 
                print('sent file')
            else:
                print("file not found")
        #Quit Connection
        elif msg == "quit":
            writing_socket.sendall("quit".encode())
            writing_socket.close()
            break
        #Send Message
        else:
            writing_socket.sendall(msg.encode())

def main():
    #Creation of writing thread
    write_id = start_new_thread(writing_function,())

    reading_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    reading_socket.bind(("localhost",0))
    reading_socket.listen(5)
    print("Reading Thread is connected at PORT: ", reading_socket.getsockname())

    print("Waiting for connection...")

    conn, addr = reading_socket.accept()

    print("Connection Established with :", addr)

    while True:
        msg = conn.recv(1024).decode()
        try:
            if not msg:
                raise ConnectionAbortedError
            #File Receive
            if msg.startswith("transfer "):
                filename = msg.split(" ")[1]
                with open(f"new{filename[0].upper()}{filename[1:]}","wb") as file:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            file.close()
                            break
                        file.write(data)
                        file.flush()
                        if len(data) < 1024:
                            break
            #Quit Connection
            elif msg == "quit":
                conn.close()
                reading_socket.close()
                break
            #Print the received message
            else:
                print("Received: ",msg)

        except ConnectionAbortedError:
            conn.close()
            reading_socket.close()
            exit()
    
    print("Terminating ...")
    exit()

if __name__ == "__main__":
    main()
