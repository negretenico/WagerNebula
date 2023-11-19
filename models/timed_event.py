from abc import ABC
from logging import info

from models.event import Event


class TimedEvent(Event, ABC):
    def __init__(self, method_to_run, method_params):
        super().__init__()
        self.method_to_run = method_to_run
        self.method_params = method_params

    def trigger(self):
        info(f"Processing event with params {self.method_params}")
        self.method_to_run(self.method_params)
