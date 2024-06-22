import requests
from http import HTTPStatus
from src.exceptions import InvalidTokenError, TelegramConnectionError, SendMessageError


def tg_send_message(tg_bot_token: str, tg_user_id: str, text: str) -> dict:
    """
    Отправка сообщения в Telegram-канал.

    :param tg_bot_token: Токен для бота
    :param tg_user_id: ID канала
    :param text: Текст сообщения
    :return: Ответ от Telegram API
    """
    base_url = 'https://api.telegram.org'
    api_url = base_url + '/bot' + tg_bot_token + '/sendMessage'
    payload = {
        'chat_id': tg_user_id,
        'text': text,
    }

    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        response_text = response.text()
        # если токен бота невалидный
        if response.status_code == HTTPStatus.UNAUTHORIZED:
            raise InvalidTokenError()
        # если ошибка сервера
        elif response.status_code >= 500:
            raise TelegramConnectionError()
        raise SendMessageError(response.status_code, response_text)
