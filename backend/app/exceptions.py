class DuplicateGoalError(Exception):
    pass


class DuplicateUserNameError(Exception):
    pass


class InvalidApiKeyError(Exception):
    pass


class InvalidTemperatureError(Exception):
    pass


class OpenAiError(Exception):
    pass


class NoGoalsFoundError(Exception):
    pass


class NoRecordsDeletedError(Exception):
    pass


class NoRecordsUpdatedError(Exception):
    pass


class UserNotFoundError(Exception):
    pass


class QuotaExceededError(Exception):
    pass
