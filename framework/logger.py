import logging
import pprint

class PrettyLogger:
    def __init__(self, name="weather_api"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "%(asctime)s.%(msecs)03d [%(levelname)s] %(name)s.%(funcName)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(ch)

    def info(self, msg, **kwargs):
        if kwargs:
            msg += "\n" + pprint.pformat(kwargs, width=120)
        self.logger.info(msg)

    def debug(self, msg, **kwargs):
        if kwargs:
            msg += "\n" + pprint.pformat(kwargs, width=120)
        self.logger.debug(msg)

    def error(self, msg, **kwargs):
        if kwargs:
            msg += "\n" + pprint.pformat(kwargs, width=120)
        self.logger.error(msg)

logger = PrettyLogger().logger
