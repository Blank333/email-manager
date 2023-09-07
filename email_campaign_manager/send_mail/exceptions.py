class SuccessException(Exception):
    def __init__(self, message="Success exception occurred. Mail already sent to user"):
        self.message = message
        super().__init__(self.message)
