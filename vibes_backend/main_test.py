#!/usr/bin/env python
import pyaudio
from Clients.audioclient import AudioClient
from time import sleep


def main():
    server = AudioClient()
    server.start_wire()
    print("here!!!!!!!!!!!!")
    sleep(2)
    server.stop_wire()


if __name__ == '__main__':
    main()