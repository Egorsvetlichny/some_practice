import logging


def simple_file_logger(name):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('logs.log')
    handler.setLevel(logging.DEBUG)
    handler.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    file_logger = simple_file_logger('simple_file_logger')

    file_logger.debug("Это сообщение уровня DEBUG")
    file_logger.info("Это сообщение уровня INFO")
    file_logger.warning("Это сообщение уровня WARNING")
    file_logger.error("Это сообщение уровня ERROR")
    file_logger.critical("Это сообщение уровня CRITICAL")