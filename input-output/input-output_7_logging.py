# Logging: flexible event logging for applications

import os
import logging
import sys

EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Basic logging", "=" * 5)

# Configure basic logging to console
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Log levels (increasing severity)
logging.debug("Debug message — detailed diagnostic info")
logging.info("Info message — confirmation of normal operation")
logging.warning("Warning message — something unexpected but still working")
logging.error("Error message — a function failed")
logging.critical("Critical message — application cannot continue")

# Log levels numeric values
print(f"DEBUG={logging.DEBUG}")  # 10
print(f"INFO={logging.INFO}")  # 20
print(f"WARNING={logging.WARNING}")  # 30
print(f"ERROR={logging.ERROR}")  # 40
print(f"CRITICAL={logging.CRITICAL}")  # 50

# Logging exceptions with traceback
try:
    result = 1 / 0
except ZeroDivisionError:
    logging.error("Division by zero occurred", exc_info=True)
    # Or equivalently:
    # logging.exception("Division by zero occurred")

# Logging with variable substitution
user = "Alice"
action = "login"
logging.info(f"User {user} performed {action}")  # f-string style
logging.info("User %s performed %s", user, action)  # % style (lazy formatting)

print("=" * 5, "File logging", "=" * 5)

# Reset logging configuration for file example
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_path = os.path.join(EXAMPLE_DIR, "app.log")

# Configure logging to both file and console
file_handler = logging.FileHandler(log_path)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.WARNING)
console_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug("This goes to file only")
logger.info("This goes to file only")
logger.warning("This goes to both file and console")
logger.error("This goes to both file and console")

# Verify log file contents
with open(log_path, "r") as f:
    print("Log file contents:")
    print(f.read())

print("=" * 5, "Logger hierarchy", "=" * 5)

# Creating hierarchical loggers
parent_logger = logging.getLogger("myapp")
child_logger = logging.getLogger("myapp.database")

# Child loggers propagate to parent
parent_logger.setLevel(logging.INFO)
child_logger.info("Child logger message")  # propagates to parent

# Preventing propagation
child_logger.propagate = False
child_logger.info("This does NOT propagate to parent")

print("=" * 5, "Rotating file handler", "=" * 5)

from logging.handlers import RotatingFileHandler

rotate_log_path = os.path.join(EXAMPLE_DIR, "rotating.log")

# Rotate when file reaches 1KB, keep 3 backup files
rotating_handler = RotatingFileHandler(
    rotate_log_path, maxBytes=1024, backupCount=3
)
rotating_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

rotate_logger = logging.getLogger("rotating_app")
for h in rotate_logger.handlers[:]:
    rotate_logger.removeHandler(h)
rotate_logger.addHandler(rotating_handler)
rotate_logger.setLevel(logging.DEBUG)

# Write enough to trigger rotation
for i in range(50):
    rotate_logger.info(f"Log entry number {i:04d} - some content here")

print(f"Rotating log exists: {os.path.exists(rotate_log_path)}")

print("=" * 5, "Timed rotating file handler", "=" * 5)

from logging.handlers import TimedRotatingFileHandler

timed_log_path = os.path.join(EXAMPLE_DIR, "timed.log")

# Rotate daily (when="midnight"), keep 7 days of backups
timed_handler = TimedRotatingFileHandler(
    timed_log_path, when="midnight", interval=1, backupCount=7
)
timed_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

# when options: "S" (seconds), "M" (minutes), "H" (hours), "D" (days), "midnight", "W0"-"W6" (weekly)

print("=" * 5, "Custom log record attributes", "=" * 5)

class CustomFormatter(logging.Formatter):
    """Custom formatter with color-like prefixes."""
    LEVEL_PREFIXES = {
        logging.DEBUG: "[DBG]",
        logging.INFO: "[INF]",
        logging.WARNING: "[WRN]",
        logging.ERROR: "[ERR]",
        logging.CRITICAL: "[CRT]",
    }

    def format(self, record):
        prefix = self.LEVEL_PREFIXES.get(record.levelno, "[???]")
        record.prefix = prefix
        return super().format(record)

custom_logger = logging.getLogger("custom")
for h in custom_logger.handlers[:]:
    custom_logger.removeHandler(h)

custom_handler = logging.StreamHandler(sys.stdout)
custom_handler.setFormatter(CustomFormatter("%(prefix)s %(asctime)s - %(message)s", datefmt="%H:%M:%S"))
custom_logger.addHandler(custom_handler)
custom_logger.setLevel(logging.DEBUG)

custom_logger.info("Custom formatted message")
custom_logger.warning("Warning with custom format")

print("=" * 5, "Logging best practices", "=" * 5)

# Use __name__ for logger names to match module hierarchy
module_logger = logging.getLogger(__name__)

# Guard expensive operations with logger.isEnabledFor
if module_logger.isEnabledFor(logging.DEBUG):
    expensive_data = "result of expensive computation"
    module_logger.debug(f"Debug data: {expensive_data}")

# Logging dict config (advanced configuration)
config_log_path = os.path.join(EXAMPLE_DIR, "dict_config.log")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": config_log_path,
            "mode": "w",
        },
    },
    "loggers": {
        "configured_app": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "propagate": True,
        },
    },
    "root": {
        "level": "WARNING",
        "handlers": ["console"],
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
configured_logger = logging.getLogger("configured_app")
configured_logger.debug("Debug to file")
configured_logger.warning("Warning to both")