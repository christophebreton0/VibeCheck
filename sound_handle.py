import sounddevice as sd
import logging
from scipy.io.wavfile import write
import jack

fs = 44100  # Sample rate
seconds = 10  # Duration of recording


class SoundHandle:

    def __init__(self, i_name='input_1', o_name='ouput_1'):
        self.client = jack.Client("VibeCheckClient")
        self.input = self.client.inports.register(i_name)
        self.output = self.client.outports.register(o_name)
        self.input_name = i_name
        self.output_name = o_name

    def activate(self):
        capture = self.client.get_ports(is_physical=True, is_output=True)
        if not capture:
            raise RuntimeError("No physical capture ports")
        else:
            self.client.activate()

    def connect(self):
        capture = self.client.get_ports(is_physical=True, is_output=True)
        for src, dest in zip(capture, self.client.inports):
            self.client.connect(src, dest)

    def terminate(self):
        self.client.activate()
        self.client.close()
