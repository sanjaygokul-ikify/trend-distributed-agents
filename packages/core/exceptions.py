class RegistrationError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)

class TaskAssignmentError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)