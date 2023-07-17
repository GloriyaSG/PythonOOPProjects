from abc import ABC, abstractmethod


class OriginalWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        pass


class Worker(OriginalWorker):

    @staticmethod
    def work():
        print("I'm working!!")

class SuperWorker(OriginalWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, OriginalWorker):
            raise AssertionError(f"`worker` must be of type {OriginalWorker}")
        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()



worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()
super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")