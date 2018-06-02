import socket
import threading
import InCent

ENCODING = 'utf-8'

port_list = [5555, 6666]
port = 4444

class Receiver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self, name=" Block receiver")

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', port))
        sock.listen(5)

        while True:
            connection, client_address = sock.accept()
            print("connection received from {}".format(str(client_address)))
            try:
                while True:
                    data = connection.recv(1024)
                    data =  data.decode(ENCODING)
                    if not data:
                        print("received block")
                        other_nodes_transactions.append(data)
                        break
            finally:
                print("exchange finished. closing connection")
                connection.shutdown(2)
                connection.close()

class Sender(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="Block sender")

    def send(self, message):
        print("sending blockchain to peers")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            for item in port_list:
                print("Sending to port", item)
                s.connect(('127.0.0.1', item))
                s.sendall(message.encode(ENCODING))
        finally:
            print("message has been sent. closing connection")
            s.shutdown(2)
            s.close()

    def run(self):
        while True:
            if len(InCent.this_nodes_transactions) != 0:
                print("sending blockchain")
                for item in InCent.this_nodes_transactions:
                    self.send(item)

def initialize():
    receiver = Receiver()
    sender = Sender()
    threads = [receiver.start(), sender.start()]

