from pythonosc import dispatcher
from pythonosc import osc_server

ip = "192.168.1.10"
port = 5000


def handler(address, args, value):
    raw_entry = 'RAW:'
    for arg in args:
        raw_entry += "," + str(arg)
    print(raw_entry)


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse", handler)

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Connecting to  " + ip + ":" + str(port))
    server.serve_forever()
