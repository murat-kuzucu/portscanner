import logging
import socket
from time import sleep

logging.basicConfig(filename='closedports.log', format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

sleep(0.60)

host = input("[+] ENTER THE TARGET IP : ")
ip = host
port_list = [80, 443, 8080, 9090]

for port in port_list:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))

    if result == 0:
        logger.info(f"{ip} {port} is open!")
        print('{ [+] Port : ', port, 'open }')
        print("----------------------------")
    else:
        logger.info(f"{ip} {port} is closed!")
        print("----------------------------")
        print('{ [!] Port : ', port, 'closed } ')
        print("----------------------------")

input("Scan is done press ENTER to EXIT!")
