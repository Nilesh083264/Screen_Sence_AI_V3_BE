import logging
import sys
from functools import lru_cache
from logging.handlers import RotatingFileHandler
from typing import Any, Dict

import structlog
from pythonjsonlogger import jsonlogger

from constants.constant import *


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any],) -> None:
        super().add_fields(log_record, record, message_dict)
        log_record['service'] = APP_NAME
        log_record['ENV'] = APP_ENV
        log_record['level'] = record.levelname
        log_record['logger'] = record.name


def configure_logging() -> None:
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    root_logger.handlers.clear()

    consol_handler = logging.StreamHandler(sys.stdout)
    consol_handler.setLevel(LOG_LEVEL)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=LOG_MAX_SIZE,
        backupCount=LOG_BACKUP_COUNT,
    )
    file_handler.setLevel(LOG_LEVEL)

    if LOG_FORMAT.lower() == "json":
        formatter = CustomJsonFormatter(
            "%(timestamp)s %(service)s %(ENV)s %(level)s %(name)s %(message)s"
        )
    else:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s -%(levelname)s - %(message)s"
        )

    consol_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(consol_handler)
    root_logger.addHandler(file_handler)
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder,
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


configure_logging()


@lru_cache()
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
