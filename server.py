import socket
import threading

IP = "127.0.0.1"
PORT = 1922


def wait(conn):
    while True:
        data = conn.recv(1024)
        data = data.decode()
        print(f"Получено: {data}")

def send(conn):
    while True:
        data = input()
        conn.send(data.encode())

with socket.socket() as server:
    server.bind((IP, PORT))
    server.listen()

    print("OK")
    conn, address = server.accept()
    print("Соединение")

    thrWait = threading.Thread(target=wait, name="THR_wait", args=(conn,))
    thrWait.start()

    thrSend = threading.Thread(target=send, name="THR_send", args=(conn,))
    thrSend.start()

    while True:
        pass