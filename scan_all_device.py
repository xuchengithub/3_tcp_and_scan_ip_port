'''
Python 扫描内网所有机器端口
'''
import socket


def main():
    ip = get_ip()
    print(f"ip: {ip}")
    pre_ip = ip.split(".", 4)
    print(f"pre_ip:{pre_ip}")
    # 获取开始IP的最后部分，并转换成整数类型
    start = 0

    # 获取结束IP的最后部分，并转换为整数类型
    end = 255

    print(f"start :{start}")
    print(f"end:{end}")
    # 从起始IP最后数字到结束IP最后数字加一遍历
    port = 50001
    for i in range(start, end+1):
        # IP的前三部分加小圆点加最后部分，组合成IP
        ip = pre_ip[0]+'.'+pre_ip[1]+'.'+pre_ip[2]+'.'+str(i)

        try:
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.settimeout(0.2)
            print(f"ip:{ip}:{port}")
            sk.connect((ip, port))
            sk.settimeout(None)
            print('Server %s port %d ok!' % (ip, port))
            sk.close()
            # 结果保存在文件中
            f = open("IP_Port.txt,", 'a')
            f.write(ip+' : '+str(port)+'\n')
            f.close()
        except:
            pass


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == '__main__':
    main()
