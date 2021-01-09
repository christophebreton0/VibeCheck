import threading
import multiprocessing
from SystemCore.baselogger import BaseLogger
from SystemCore.baseinterface import BaseInterface
import abc


class BaseClient(BaseLogger, threading.Thread, metaclass=abc.ABCMeta):
    def __init__(self, name: str, id_t):
        if isinstance(id_t, int):
            name += str(id_t)
        self._id = id_t
        self._interface = None
        self._local_terminate_switch = multiprocessing.Event()
        threading.Thread.__init__(self, name=name, daemon=True)
        BaseLogger.__init__(self, name)

    @property
    def id(self) -> int:
        return self._id

    @property
    def interface(self):
        return self._interface

    def set_interface(self, interface: BaseInterface):
        assert isinstance(interface, BaseInterface), 'Your interface should inherit from BaseInterface class'
        self._interface = interface
        BaseLogger.set_logger_interface(self, interface)
        self.set_logger_function_call(self._interface.put_std_message)
        return self

    @property
    def get_name(self) -> str:
        return threading.Thread.getName(self)

    # THREAD method
    def run(self) -> None:
        """ Thread execute the run function after start has called """
        assert self._interface is not None, 'Interface not set.'
        BaseLogger._start_logger(self)
        self.debug('begin')
        self.on_enter()
        while not self.is_terminate():
            try:
                self.main_loop()
            except Exception as err:
                if not self.is_terminate():
                    self.error("[{}] {}".format(type(err).__name__, err))
        self.on_exit()
        self.debug('end')

    def on_enter(self) -> None:
        """ optional """
        pass

    def on_exit(self) -> None:
        """ optional """
        pass

    @abc.abstractmethod
    def main_loop(self) -> None:
        raise NotImplementedError()

    def terminate(self) -> None:
        """ Set the terminate flag for the current system """
        self._local_terminate_switch.set()
        self.debug('Terminate')

    def is_terminate(self) -> bool:
        """ Check if the terminate flag is set  """
        return self._local_terminate_switch.is_set()

    def start(self) -> None:
        """ Start the run method and set global and local terminate flag """
        self._local_terminate_switch.clear()
        threading.Thread.start(self)
