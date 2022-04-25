from pythonosc import dispatcher
from pythonosc import osc_server
from .. import muse

ip = '0.0.0.0'
port = 5000


def eeg_hadler(data):
    if data is not None:
        print(data.__dict__)


if __name__ == "__main__":
    muse = muse.Muse('0.0.0.0', 5000)
    muse.add_listener(muse.DataType.EEG, eeg_hadler())
