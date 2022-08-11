class InvalidLetterException(Exception):
    """Exception raised for errors with the format letter.

    Attributes:
        message: str
            Explanation of the error
    """
    def __init__(self, 
                 message="The input introduced is invalid, must be a single letter not a number or multiple letters."):
        self.message = message
        super().__init__(self.message)

class TooManyArgsException(Exception):
    pass

class InvalidWordException(Exception):
    pass

class InvalidLangDictException(Exception):
    pass