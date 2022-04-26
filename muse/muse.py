from pythonosc import dispatcher
from pythonosc import osc_server
from enum import Enum


class DataType(Enum):
    EEG = 1
    GYROSCOPE = 2
    ACCELEROMETER = 3


class MuseData(object):
    def __init__(self, data_type, data):
        self.type = data_type
        self.data = data


class EEG(MuseData):
    def __init__(self, *args):
        super(EEG, self).__init__(DataType.EEG, args)

    def get_channel(self, channel_number):
        return self.data[channel_number - 1]

    def channel_count(self):
        return len(self.data)


class Gyroscope(MuseData):
    def __init__(self, *args):
        super(Gyroscope, self).__init__(DataType.GYROSCOPE, args)

    def get_x(self):
        return self.data[0]

    def get_up_down_location(self):
        return self.get_x()

    def get_y(self):
        return self.data[1]

    def get_tilt(self):
        return self.get_y()

    def get_z(self):
        return self.data[2]


class Accelerometer(MuseData):
    def __init__(self, *args):
        super(Accelerometer, self).__init__(DataType.ACCELEROMETER, args)

    def get_x(self):
        return self.data[0]

    def get_left_right_pitch_acc(self):
        return self.get_x()

    def get_y(self):
        return self.data[1]

    def get_up_down_acc(self):
        return self.get_y()

    def get_z(self):
        return self.data[2]

    def get_left_right_acc(self):
        return self.get_y()


addresses = []


class Muse:
    listeners = {}

    def add_listener(self, data_type, data_arrived_func):
        if data_type not in self.listeners.keys():
            self.listeners[data_type] = [data_arrived_func]
        else:
            self.listeners[data_type].append[data_arrived_func]

    def notify_listeners(self, data):
        if data.type in self.listeners.keys():
            for callback in self.listeners:
                callback(data)

    def handler(self, address: str, *args):
        if address.endswith('eeg'):
            self.notify_listeners(EEG(args))
        elif address.endswith('gyro'):
            self.notify_listeners(Gyroscope(args))
        elif address.endswith('acc'):
            self.notify_listeners(Accelerometer(args))


        if address not in addresses:
            addresses.append(address)
            print(address)
        raw_entry = str(address) + ':'
        for arg in args:
            raw_entry += "," + str(arg)
        # print(raw_entry)

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        disp = dispatcher.Dispatcher()
        dispatcher.map("/*", self.handler)
        print("Connecting to  " + ip + ":" + str(port))
        server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
        print("Connected")
        server.serve_forever()


if __name__ == "__main__":
    muse = Muse('0.0.0.0', 5000)
