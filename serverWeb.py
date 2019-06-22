from socket import *
import sys
 
porta = 55555 # Atribuindo um valor de porta 
 
serverSocket = socket(AF_INET, SOCK_STREAM) # Criando um socket tcp
serverSocket.bind(('localhost',porta)) 

serverSocket.listen(1) # Limita a conexão a 1 cliente

# forreach foi desnecessario 

while True:  # espera um conexão
   
    connectionSocket, address = serverSocket.accept() 
    requisicao = connectionSocket.recv(1024).decode('utf-8')

    requisicao = requisicao.split(' ') #Separa toda a requisição por espaços 
    arquivo_req = requisicao[1].lstrip('/') # Passa nome do arquivo solicitado sem a /, poderia usar o cod abaixo;

    #filename = message.split()[1] 
    #f = open(filename[1:])

   
    try:
        arquivoHTML = open(arquivo_req) #abrir o arquivo
        message = arquivoHTML.read()
        arquivoHTML.close()
 
        header = 'HTTP/1.1 200 OK\n Content-Type: text/html\n\n'
 
    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n Content-Type: text/html\n\n'
        notFound = open('404.html')
        message = notFound.read()
        notFound.close()
        #message = '<html><body><h1>Error 404: File not found</h1></body></html>'.encode('utf-8')
 
    messageFinal = header.encode('utf-8')
    messageFinal += message.encode()
    connectionSocket.send(messageFinal)
    connectionSocket.close()
sys.close()
