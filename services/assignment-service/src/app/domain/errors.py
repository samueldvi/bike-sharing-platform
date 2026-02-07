class DomainError(Exception):
    code: str = "DOMAIN_ERROR"

    def __init__(self, message: str):
        super().__init__(message)


class ConflictError(DomainError):
    code = "CONFLICT"


class NotFoundError(DomainError):
    code = "NOT_FOUND"
