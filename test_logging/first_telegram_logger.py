import datetime
import logging

import requests


class TelegramHandler(logging.Handler):
    """Handler для отправки логов в Telegram."""

    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def send_message_to_telegram(self, message: str):
        """Отправляет сообщене с логами в Telegram"""

        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        data = {'chat_id': self.chat_id, 'text': message}
        requests.post(url=url, json=data)

    def emit(self, record):
        """Регистрирует запись лога.

        Данный метод защищён от возможных ошибок, чтобы ошибка при логгировании не повлияла на работу кода."""

        try:
            message = self.format(record)
            self.send_message_to_telegram(message)
        except RecursionError:
            raise
        except Exception:
            self.handleError(record)


def create_tg_logger(name):
    """Создаёт Telegram Logger"""

    telegram_token = '6597088180:AAH0yCd3bj1KDhI17t7-Js5SH-7rwLDo2iM'
    chat_id = -4044943020

    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    handler = TelegramHandler(telegram_token, chat_id)
    handler.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    logger = create_tg_logger('test_telegram_logger')

    time = datetime.datetime.now()
    logger.info("Что-то произошло! Это сообщение уровня INFO")
    logger.debug("Это сообщение уровня DEBUG")
    logger.warning("Это сообщение уровня WARNING")
    logger.error("Это сообщение уровня ERROR")
    logger.critical("Это сообщение уровня CRITICAL")
    print(datetime.datetime.now() - time)
