from typing import TypeVar, Generic, Any

T = TypeVar('T')  # Declare a type variable


class Result(Generic[T]):
    def __init__(self):
        self.__data: T = None
        self.__error: Any = None

    def failed(self) -> bool:
        return self.__error is not None

    def success(self) -> bool:
        return self.__error is None

    def set_error(self, msg) -> None:
        self.__error = msg

    def set_data(self, data: T) -> None:
        self.__data = data

    def data(self):
        return self.__data

    def error(self):
        return self.__error
