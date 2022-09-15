import socket, os

def cwd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(4096).decode()
    print("Current Working Directory: ", response)
    client_socket.close()
        

def ls(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(1024).decode()
    response = eval(response)
    print("All files in this directory:")
    print(*response, sep = "\n")
    client_socket.close()

def cd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    response = client_socket.recv(1024).decode()
    print(response)
    if (response == "OK"):
        curr = client_socket.recv(1024).decode()
        print("Path is changed to:", curr)
    else:
        print("Path isn't changed")
    client_socket.close()

def dwd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    status = client_socket.recv(1024).decode()
    cmd = cmd.split(" ")
    print("Status:", status)
    if (status == "OK"):
        with open("dwd"+cmd[1]+cmd[2], 'wb') as file_to_write:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file_to_write.write(data)
            file_to_write.close()
    client_socket.close()

def upd(cmd):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.send(cmd.encode())
    cmd = cmd.split(" ")
    try:
        with open(cmd[1], 'rb') as file_to_send:
            client_socket.send("OK".encode())
            print("Status: OK")
            data=file_to_send.read(1024)
            while(data):
                client_socket.send(data)
                data=file_to_send.read(1024)
                file_to_send.close()
    except:
        client_socket.send("NOK".encode())
        print("Status: NOK")
    client_socket.close()

def client_program():
    global host, port
    host = socket.gethostname()
    port = 5000
    print("Connection is Established with", host)

    cmd = str(input("-> "))
    
    while cmd.lower().strip() != 'exit':
        cmd_list = cmd.split(" ")
        if (cmd_list[0] == "cwd"):
            cwd(cmd)
        elif (cmd_list[0] == "ls"):
            ls(cmd)
        elif (cmd_list[0] == "cd"):
            cd(cmd)
        elif (cmd_list[0] == "dwd"):
            dwd(cmd)
        elif (cmd_list[0] == "upd"):
            upd(cmd)

        cmd = str(input("-> "))


if __name__ == '__main__':
    client_program()