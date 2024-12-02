import socket

# Параметры сервера
HOST = '0.0.0.0'  # Прослушивание на всех интерфейсах
PORT = 8081       # Порт 8080

# Создание сокета
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))  # Привязываем сокет к адресу и порту
    server_socket.listen(5)          # Максимум 5 подключений в очереди
    print(f"Сервер запущен на {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server_socket.accept()  # Принимаем подключение
        with client_socket:
            print(f"Подключение от {client_address}")
            # Отправляем ответ клиенту
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
            client_socket.sendall(response.encode('utf-8'))
            print(f"Сообщение отправлено клиенту {client_address}")
