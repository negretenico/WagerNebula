from abc import ABC, abstractmethod


class Event(ABC):
    @abstractmethod
    def trigger(self):
        pass
