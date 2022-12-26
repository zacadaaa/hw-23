class BaseError(Exception):
    message = 'Unknown error'


class QueryError(BaseError):
    message = 'Invalid query'


class FilePathError(BaseError):
    message = 'Invalid File-path'