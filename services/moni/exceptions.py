class APINotConfiguredError(Exception):
    def __init__(self, message="La API no está configurada correctamente."):
        self.message = message
        super().__init__(message)


class APIValidationError(Exception):
    def __init__(self, field):
        self.message = f"{field} es inválido"
        super().__init__(self.message)
