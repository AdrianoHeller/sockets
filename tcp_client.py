import socket

target_host = 'www.google.com'
target_port = 80

message = 'GET / HTTP/1.1\rHost:google.com\r\n\r\n'

# cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# cria a conexao do cliente
client.connect((target_host, target_port))

# envia alguns dados
client.send(message)

# recebe alguns dados
response = client.recv(4096)

print(f'Response: {response}')