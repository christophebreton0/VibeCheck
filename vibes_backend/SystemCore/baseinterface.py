import abc
from SystemCore.baselogger import BaseLogger
import logging


class BaseInterface(BaseLogger, metaclass=abc.ABCMeta):
    def __init__(self, name):
        BaseLogger.__init__(self, name)

    def put_std_message(self, std_container: logging.LogRecord) -> logging.LogRecord:
        return std_container
