class EmailAlreadyExistError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'User already exists.'}
        super().__init__(self.message)

class WrongFieldsError(Exception):
    pass
   
class DontIncludedDataError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'Email or nome not included'}
        super().__init__(self.message)