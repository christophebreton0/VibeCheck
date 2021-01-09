import abc
import logging


class StreamModelHandler(logging.Handler):
    def __init__(self, level=logging.INFO):
        logging.Handler.__init__(self, level=level)
        self._interface = None
        self._func = None

    def emit(self, record):
        if self._func is not None:
            self._func(record)
        elif self._interface is not None:
            self._interface.put_std_message(record)

    def set_interface(self, interface_method):
        self._interface = interface_method

    def set_function(self, func):
        self._func = func


class BaseLogger(metaclass=abc.ABCMeta):
    def __init__(self, name: str) -> None:
        self._logger = logging.getLogger(name)
        self._init_level = logging.INFO

        self._handler_console = logging.StreamHandler()
        self._handler_model = StreamModelHandler()

        # Initialization
        self._start_logger()

    def set_logger_interface(self, interface):
        self._handler_model.set_interface(interface)

    def set_logger_function_call(self, func):
        self._handler_model.set_function(func)

    # INITIALIZER
    def _start_logger(self):
        """ Start logger by creating a console handler """
        self._logger.setLevel(logging.DEBUG)

        self._handler_console.setLevel(self._init_level)
        _formatter = logging.Formatter('[%(levelname)s] %(relativeCreated)d - %(name)s.%(funcName)s : %(message)s')
        self._handler_console.setFormatter(_formatter)
        self._logger.addHandler(self._handler_console)

        self._handler_model.setLevel(logging.INFO)
        self._logger.addHandler(self._handler_model)

    def _close_logger(self):
        """ Start logger by removing the current console handler """
        self._logger.removeHandler(self._handler_console)
        self._logger.removeHandler(self._handler_model)
        self._handler_console.close()
        self._handler_model.close()

    # LOGGING method
    @property
    def info(self):
        """ Class wrapper to send a message with INFO level to the logger """
        return self._logger.info

    @property
    def debug(self):
        """ Class wrapper to send a message with DEBUG level to the logger """
        return self._logger.debug

    @property
    def warning(self):
        """ Class wrapper to send a message with WARNING level to the logger """
        return self._logger.warning

    @property
    def error(self):
        """ Class wrapper to send a message with ERROR level to the logger """
        return self._logger.error

    @property
    def critical(self):
        """ Class wrapper to send a message with CRITICAL level to the logger """
        return self._logger.critical

    @property
    def log(self):
        """ Class wrapper to send a message with a specific level to the logger """
        return self._logger.log

    @property
    def set_level(self):
        """ Class wrapper to set the logger level display """
        return self._handler_console.setLevel

    def disable_logging(self):
        self._logger.removeHandler(self._handler_console)

    def enable_logging(self):
        self._logger.addHandler(self._handler_console)

    def __del__(self):
        self._close_logger()
        del self