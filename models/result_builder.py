from models.result import Result


class ResultBuilder:
    def __init__(self):
        self.result = Result()

    @classmethod
    def error(cls, error) -> 'ResultBuilder':
        instance = cls()
        instance.result.set_error(error)
        return instance

    @classmethod
    def data(cls, data) -> 'ResultBuilder':
        instance = cls()
        instance.result.set_data(data)
        return instance

    def build(self):
        return self.result
