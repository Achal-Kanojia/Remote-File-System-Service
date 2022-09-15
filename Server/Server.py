import socket, os
from pathlib import Path

def encrypt(text, s): 
    text = text.strip()
    result = "" 
    for i in range(len(text)): 
        char = text[i]
        if (char == " "):
            result += " "
        elif (char.isnumeric()):
            temp = ord(str((int(char)+s)%10))
            result += chr(temp)
        elif (char.isupper()): 
            temp = (ord(char) + s-65) % 26 + 65
            result += chr((ord(char) + s-65) % 26 + 65) 
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result 

def reverse(text): 
    new_data = ""
    for word in text.split():
        rev_word = word[::-1]
        new_data += rev_word
        new_data += " "
    return new_data

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Server is Active and listening at port:", port)


    while True:
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        if not data:
            break
        
        data = data.split(" ")
        if (data[0] == 'cwd'):
            conn.send(os.getcwd().encode())
        elif (data[0] == 'ls'):
            y = str(os.listdir())
            conn.send(y.encode())
        elif (data[0] == 'cd'):
            try:
                path = Path(data[1])
                os.chdir(path)
                conn.send("OK".encode())
                conn.send(os.getcwd().encode())
            except OSError:
                conn.send("NOK".encode())
        elif (data[0] == 'dwd'):
            try:
                with open(data[1], 'rb') as file_to_send:
                    conn.send("OK".encode())
                    for word in file_to_send:
                        if (data[2] == "plain"):
                            conn.sendall(word)
                        elif (data[2] == "substitute"):
                            conn.sendall(encrypt(word.decode(), 2).encode())
                            conn.sendall("\n".encode())
                        elif (data[2] == "reverse"):
                            conn.sendall(reverse(word.decode()).encode())
                            conn.sendall("\n".encode())
            except:
                conn.send("NOK".encode())
        elif (data[0] == 'upd'):
            status = conn.recv(1024).decode()
            if (status == "OK"):
                with open("upd"+data[1], 'wb') as file_to_write:
                    data=conn.recv(1024)
                    while True:
                        if not data:
                            break
                        else:
                            file_to_write.write(data)
                            data=conn.recv(1024)
                        file_to_write.close()
                        break
        conn.close()


if __name__ == '__main__':
    server_program()