import os
import logging
from threading import Thread
from sound_handle import SoundHandle
from http.server import SimpleHTTPRequestHandler

PORT = 8080
HOST = 'localhost'


class ServerHandle(SimpleHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        t_sound = Thread()
        t_blender = Thread()
