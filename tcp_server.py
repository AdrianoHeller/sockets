import socket
import threading

bind_ip = '0.0.0.0'

bind_port = '9999'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.listen(5)

print('[*] Listening on %s:%d' % (bind_ip, bind_port))

# define thread para tratamento dos clients


def handle_client(client_socket):

    # exibe o envio do client
    request = client_socket.recv(1024)

    print('[*]Received %s' % request)

    # envia um pacote de volta
    client_socket.send('ACK')

    # fecha o socket
    client_socket.close()


while True:

    client, addr = server.accept()

    print('[*]Accepted connection from %s:%d' % (addr[0], addr[1]))

    # coloca a thread do client em acao pra aceitar a entrada de dados
    client_handler = threading.Thread(target=handle_client, args=(client,))

    client_handler.start()
