class TelegramBotException(Exception):
    """Базовое исключение для всех ошибок, связанных с Telegram Bot Client."""

    pass


class SendMessageError(TelegramBotException):
    """Ошибка при отправке сообщения."""

    def __init__(self, status_code, message) -> None:
        super().__init__(f'Failed to send message: HTTP {status_code} {message}')
        self.status_code = status_code
        self.message = message


class InvalidTokenError(TelegramBotException):
    """Ошибка неверного токена."""

    def __init__(self) -> None:
        super().__init__('Invalid bot token provided.')


class TelegramConnectionError(TelegramBotException):
    """Ошибка соединения с сервером Telegram."""

    def __init__(self) -> None:
        super().__init__('Failed to connect to Telegram server.')
