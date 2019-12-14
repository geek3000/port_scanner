import socket
import json

hote = "localhost"

port_info_json=""

print("---------------Geek3000 Port scanner-------------------------")
print("---------------")
print("---------------")
print("Loading defauld port information file ...")

with open("./ports.json", "r") as port_info:
    port_info_json=json.loads(port_info.read())


print("---------------Start scanning port ...")
for port in port_info_json:
    try:
        print("Scanning port {0}".format(port))
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((hote, int(port)))
        print("Openned {0}  {1}".format(port, port_info_json[port][0]['description']))
        connection.close()
    except ConnectionRefusedError:
        pass
    except TimeoutError:
        pass
    except KeyboardInterrupt:
        pass

print("Bye Bye")
connection.close()
