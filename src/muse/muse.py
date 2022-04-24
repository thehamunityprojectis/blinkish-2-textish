from pythonosc import dispatcher
from pythonosc import osc_server


class MuseData(object):
    def __init__(self, data_type, data):
        self.type = data_type
        self.data = data


class EEG(MuseData):
    def __init__(self, *args):
        super(EEG, self).__init__('EEG', args)

    def get_channel(self, channel_number):
        return self.data[channel_number - 1]

    def channel_count(self):
        return len(self.data)


class Gyroscope(MuseData):
    def __init__(self, *args):
        super(Gyroscope, self).__init__('Gyroscope', args)


ip = '0.0.0.0'
port = 5000
addresses = []


def handler(address: str, *args):
    if address.endswith('eeg'):
        data = EEG(args)
    elif address.endswith('gyro'):
        data = Gyroscope(args)
        print(data.__dict__)
    if address not in addresses:
        addresses.append(address)
        print(address)
    raw_entry = str(address) + ':'
    for arg in args:
        raw_entry += "," + str(arg)
    # print(raw_entry)


if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    # dispatcher.map("/muse/eeg", handler)
    dispatcher.map("/*", handler)
    print("Connecting to  " + ip + ":" + str(port))
    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Connected")
    server.serve_forever()
