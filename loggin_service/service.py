from uvicorn.config import LOGGING_CONFIG
import logging.config
import logging

def get_logger(name: str) -> logging.Logger:
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(levelprefix)s [%(name)s] %(message)s"
    LOGGING_CONFIG["loggers"][name] = {
        "handlers": ["default"],
        "level": "INFO",
        "propagate": False,
    }
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger(name)