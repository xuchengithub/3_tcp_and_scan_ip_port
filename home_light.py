# coding=utf-8
import socket


def main():
    while True:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 要发送的ip地址和端口（元组的形式）
        send_addr = ('192.168.222.217', 50001)
        print('send_addr = ', send_addr)
        udp_socket.connect(send_addr)

        string = str(input('weclome please input witch switch:'))
        # 要发送的信息
        b = bytes(string, encoding='utf-8')
        udp_socket.send(b)

        udp_socket.close()


if __name__ == "__main__":
    main()
