from enum import Enum
class ResponseStatus(Enum):
    ACCOUNT_NEED_VERIFY = 36
    IP_NEED_VERIFY = 35
    SERVER_ERROR_CLASSIFY = 1000
    SUCCESS = 0
    TOKEN_ERROR = 7
    TOKEN_ERROR_31 = 31
    TOKEN_ERROR_32 = 32
    VALIDATION_ERROR = 5