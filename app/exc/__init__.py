class EmailAlreadyExistError(Exception):
    def __init__(self) -> None:
        self.message = {'error': 'User already exists.'}
        super().__init__(self.message)

class WrongFieldsError(Exception):
    pass
   
