#Author = Murat Kuzucu
import logging
import socket

logging.basicConfig(filename='closedports.log', format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


host = input("[+] ENTER THE TARGET IP : ")
ip = host
port_list = [80, 443, 8080, 9090]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        print(f"{ip} {port} is open!")
        print("----------------------------")
    else:
        logger.info(f"{ip} {port} is closed!")  # If ports are closed write to file!
        print("----------------------------")
        print(f"{ip} {port} is closed!")
        print("----------------------------")

input("Scan is done press ENTER to EXIT!")
