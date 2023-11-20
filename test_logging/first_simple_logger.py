import logging


def create_simple_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(level=logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == '__main__':
    first_logger = create_simple_logger('first_simple_logger')

    first_logger.debug("Это сообщение уровня DEBUG")
    first_logger.info("Это сообщение уровня INFO")
    first_logger.warning("Это сообщение уровня WARNING")
    first_logger.error("Это сообщение уровня ERROR")
    first_logger.critical("Это сообщение уровня CRITICAL")
