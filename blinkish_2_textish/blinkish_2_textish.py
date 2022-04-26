from pythonosc import dispatcher
from pythonosc import osc_server
#import sys
#sys.path.insert(0, 'src/blinkish
#from muse import Muse
import muse
ip = '0.0.0.0'
port = 5000


def eeg_hadler(data):
    if data is not None:
        print(data.__dict__)


if __name__ == "__main__":
    dir(muse.Muse)
#    myMuse = muse.Muse('0.0.0.0', 5000)
#    myMuse.add_listener(muse.DataType.EEG, eeg_hadler())
