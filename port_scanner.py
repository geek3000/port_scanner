import socket
import json
from termcolor import colored

hote = "localhost"

port_info_json=""

print(colored("---------------Geek3000 Port scanner-------------------------", "red"))
print(colored("---------------", "red"))
print(colored("---------------", "red"))
print(colored("Loading defauld port information file ...", "blue"))

with open("./ports.json", "r") as port_info:
    port_info_json=json.loads(port_info.read())


print(colored("---------------Start scanning port ...", "red"))
for port in port_info_json:
    try:
        print(colored("Scanning port: ", 'green'), colored(port, 'yellow'))
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((hote, int(port)))
        print(colored("Openned {} ".format(port), "red"), colored(port_info_json[port][0]['description'], "blue"))
        connection.close()
    except ConnectionRefusedError:
        pass
    except TimeoutError:
        pass
    except KeyboardInterrupt:
        exit(0)

print("Bye Bye")
connection.close()
