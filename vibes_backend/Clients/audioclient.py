import pyaudio
import numpy as np
from SystemCore.baseclient import BaseClient



WIDTH = 2
CHUNK = 2048
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 1


class AudioClient(BaseClient):

    def __init__(self, sample_time=RECORD_SECONDS):
        super().__init__(id_t="audio", name='AudioClient')
        self.server = pyaudio.PyAudio()
        self.stream = None
        self.sample_time = sample_time

    def start_wire(self):
        print("*** recording")
        num_frames = int(RATE*self.sample_time/CHUNK)
        data_array = np.zeros(num_frames, dtype=np.int16)
        self.stream = self.server.open(format=pyaudio.paInt16,
                                       channels=CHANNELS,
                                       rate=RATE,
                                       input=True,
                                       output=True,
                                       frames_per_buffer=CHUNK)

        for i in range(0, int(RATE/CHUNK*self.sample_time)):
            data = np.fromstring(self.stream.read(CHUNK), dtype=np.int16)
            peak = np.average(np.abs(data)) * 2
            bars = "#" * int(50 * peak / 2 ** 12)
            print("%04d %05d %s" % (i, peak, bars))

    def stop_wire(self) -> bool:
        if self.stream.is_active():
            self.stream.stop_stream()
            self.stream.close()

            print("*** done")

            self.server.terminate()
            return True
        else:
            return False

    def main_loop(self) -> None:
        pass
