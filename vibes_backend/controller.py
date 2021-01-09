import logging
import os
import time
import importlib

from Clients.audioclient import AudioClient
from Clients.blenderclient import BlenderCLient


class AudioController:

    def __init__(self):
        self._cli_audio = None
        self._cli_blender = None

        self._int_audio = None
        self._int_blender = None

        self._mod_audio = None
        self._mod_blender = None
        self._mod_web_srv = None

    def _init_clients(self):
        self._cli_audio = AudioClient()
        self._cli_blender = BlenderCLient()

    def _init_interfaces(self):
        pass

    def _init_models(self):
        pass

    def _start_clients(self):
        self._cli_audio.start()
        self._cli_blender.start()

    def terminate(self):
        self._cli_audio.stop()
        self._cli_blender.stop()

    def
