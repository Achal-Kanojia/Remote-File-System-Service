# DESIGN DOCUMENT

This repository contains a Simple Remote File System (RFS) service application developed using Socket Programming in Python. <br>
This RFS service application allows the client to perform the following five commands: <br>

| Command        | Description                                                       | Status  |
| ---------------| ------------------------------------------------------------------| ------- |
| cwd            | Retrieve the path of the current working directory of the server  |         |
| ls             | List the files/folders present in the cwd of the server           |         |
| cd 'dir'       | Change the directory to 'dir' as specified by the client          |  OK/NOK |
| dwd 'file'     | Download the <file> specified by the user on server to client     |  OK/NOK |
| upd 'file'     | Upload the 'file' on client to the remote server in CWD           |  OK/NOK |

## Structure

### 1. Client
- Client.py: Contains the code for the client.
- UploadFile.txt: The file used for testing the functionality of upd command.
- dwdSample.txtplain: The file downloaded from the server to the client without any change.
- dwdSample.txtreverse: The file downloaded from the server to the client with Transpose.
- dwdSample.txtsubstitute: The file downloaded from the server to the client with Caesar Cipher.
### 2. Server
- Server.py: Contains the code for the server.
- Sample.txt: The file used for testing the functionality of dwd command.
- updUploadFile.txt: File uploaded from the client to the server.

## Flow of working for Client and Server

### Client
  - Creating a Transmission Control Protocol (TCP) socket.
  - Connect to the server.
  - The connection establishes between Client and Server.
  - Take commands from the input and send them to server.
  - Receives information from the server and provide output.

### Server
  - Creating a Transmission Control Protocol (TCP) socket.
  - Bind the socket to the Host and Port.
  - Wait for the client to request the connection.
  - The connection establishes between Server and Client.
  - Follow the commands given by the user at client end.

##  Layer N model of the RFS client and server

### **Layer N: File Service (Content)**
This layer supports the execution of commands between the client and the server. Using the Crypto Service offered by the N-1 Layer, File Service encrypts (encodes) and decrypts (decodes) the data to be exchanged between the client and server. Additionally, Some OS Commands (such as getcwd(), listdir(), and chdir()) are used by this layer to execute required actions.

### **Layer N-1: Crypto Service**
This layer facilitates three different modes (Plain Text, Substitute, Transpose modes) that can be used by the File Service to encrypt the data before transmitting to the Networking Layer. The three encryption modes are:
1. **Plain Text:** No change to the input; (No encryption or decryption).
2. **Substitute:** Only alphanumeric characters will be substituted with fixed offset, say Caesar cipher with offset two. **Eg:** *Ak19* encodes to *Cm31*
3. **Transpose:** Reverse the contents in a word by word manner. **Eg:** *Computer Networks* will be transposed to *retupmoC skrowteN*

### Layer N-2: Networking (TCP)
In this layer, Transmission Control Protocol (TCP) is used for exchanging the information between client and server. It ensures the the successful exchange of data sent in the form of packets between client and server.
<br>

## Commands
**0. Basic Connection** <br>
*Files Initially Present in Client Folder* <br>
![image](https://user-images.githubusercontent.com/79503913/190490200-6c829b8d-442b-42a4-bd36-79d362fbcab9.png)
<br>
*Files Initially Present in Server Folder* <br>
![image](https://user-images.githubusercontent.com/79503913/190490258-45ed5d61-b2d4-4eda-b2c7-4739fb7541d6.png)
<br>
*Activating Server* <br>
![image](https://user-images.githubusercontent.com/79503913/190490313-e23234af-db89-4867-8c68-d01a05950e34.png)
<br>
*Establishing Connection with Host* <br>
![image](https://user-images.githubusercontent.com/79503913/190486275-f8b76b44-fef1-4171-90e0-db616ed977d9.png) <br>
<br>
**1. cwd** <br>
*Syntax: cwd* <br>
*Functionality: Retrieve the path of the current working directory for the user.* <br>
![image](https://user-images.githubusercontent.com/79503913/190486643-3d232ccc-dace-4e67-b5b1-02225dff0b77.png) <br>
**2. ls** <br>
*Syntax: ls* <br>
*Functionality: List the files/folders present in the cwd of the server.* <br>
![image](https://user-images.githubusercontent.com/79503913/190486867-b7bf1a0a-9648-4709-b6b0-4b062b196d86.png) <br>
**3. cd** <br>
*Syntax: cd 'dir'* <br>
*Functionality: Change the directory to 'dir' as specified by the client.* <br>
![image](https://user-images.githubusercontent.com/79503913/190487006-846bcae5-d25e-4a9a-a2cb-49e8cf004cad.png) <br>
![image](https://user-images.githubusercontent.com/79503913/190487039-395a312a-8aaa-4089-a722-19eb119e9c16.png) <br>
**4. dwd** <br>
*Syntax: dwd 'file' 'CryptoMode'* <br>
*Functionality: Download the <file> specified by the user on server to client based on the chosen crypto mode.* <br>
  ![image](https://user-images.githubusercontent.com/79503913/190487914-b2d00869-b60b-445f-862a-16aa67373c39.png) <br>
- Plain <br>
  ![image](https://user-images.githubusercontent.com/79503913/190487776-89d2c002-3c65-452c-92ed-9fb0cec9f05c.png) <br>
![image](https://user-images.githubusercontent.com/79503913/190487794-0998ecd3-1bee-4640-85b9-98566ba8eb56.png) <br>
- Substitute <br>
  ![image](https://user-images.githubusercontent.com/79503913/190487954-74def1a5-4ff0-415d-9eb9-a77d3868ef7c.png) <br>
![image](https://user-images.githubusercontent.com/79503913/190487964-c900ea1f-f64a-4ba5-baba-6487efd7ecba.png) <br>
- Transpose <br>
![image](https://user-images.githubusercontent.com/79503913/190488028-33d27167-dd1f-486c-92c5-b85c3c4eaa34.png) <br>
![image](https://user-images.githubusercontent.com/79503913/190488054-51a014ff-5e41-4a98-8333-57850f6d6469.png) <br>
<br>

**5. upd** <br>
*Syntax: upd 'file'* <br>
*Functionality: Upload the 'file' on client to the remote server in CWD.* <br>
![image](https://user-images.githubusercontent.com/79503913/190490055-7b24f766-3eed-494f-a808-a0739387097b.png) <br>
  ![image](https://user-images.githubusercontent.com/79503913/190490097-dd3c947e-d0f4-41da-a98c-a7557ad378a7.png) <br>
