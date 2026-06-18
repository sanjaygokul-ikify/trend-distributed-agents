from typing import Any

class TrendAgentError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class TrendAgentTypeError(TrendAgentError):
    def __init__(self, message: str):
        super().__init__(message)


class TrendAgentValueError(TrendAgentError):
    def __init__(self, message: str):
        super().__init__(message)
