from socket import *
import random#ALICE
import regers
HOST=''
PORT=8090
sockobj=socket(AF_INET,SOCK_STREAM)
sockobj.bind((HOST,PORT))
sockobj.listen(5)
v=regers.v
k=regers.k
g=regers.g
N=regers.N
while True:
    connection,adress=sockobj.accept()
    print('Connected to:',adress)
    while True:
        data=connection.recv(1024)#I
        if not data:break
        I=str(data)
        connection.send(b'accept')
        data=connection.recv(1024)#a
        a=int(data)
        connection.send(b'accept')
        data=connection.recv(1024)#A
        A=int(data)
        b=random.randint(0,1231)
        #B=(regers.k*regers.v+regers.g^b%regers.N)%regers.N
        B=(k*v + g^b % N) % N
        connection.send(str.encode(str(B)))
        u=regers.Hash(A,B)
        if u==0:
            connection.close()
        #S=((A*((regers.v^u)%regers.N))^b)%regers.N
    
        S = ((A*((v^u) % N)) ^ b) % N
        connection.send(str.encode(str(S)))

        K=regers.Hash(S,1)
        data=connection.recv(1024)
        if not data:break
        K1=int(data)
        if K1==K:
            print('User is logging in')
        print(K)
    connection.close()
