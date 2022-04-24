from pythonosc import dispatcher
from pythonosc import osc_server

ip = '0.0.0.0'
port = 5000
addresses = []

def handler(address: str, *args):
    if address not in addresses:
        addresses.append(address)
        print(address)
    raw_entry = str(address) + ':'
    for arg in args:
        raw_entry += "," + str(arg)
    #print(raw_entry)


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/muse/eeg", handler)
    dispatcher.map("/*", handler)
    print("Connecting to  " + ip + ":" + str(port))
    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Connected")
    server.serve_forever()
