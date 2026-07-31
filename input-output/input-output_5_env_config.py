# Environment variables and configuration

import os

# Create examples directory
EXAMPLE_DIR = os.path.join(os.path.dirname(__file__), "examples")
os.makedirs(EXAMPLE_DIR, exist_ok=True)

print("=" * 5, "Environment variables", "=" * 5)

# Reading environment variables
# os.getenv() returns None if not found (no KeyError)
home = os.getenv("HOME") or os.getenv("USERPROFILE")
print(f"Home: {home}")

path_var = os.getenv("PATH", "/usr/bin")  # default value
print(f"PATH length: {len(path_var)} chars")

# os.environ is a dict-like mapping
# os.environ["VAR"] raises KeyError if not set
# os.getenv("VAR") returns None if not set
# os.getenv("VAR", "default") returns default if not set

# Setting environment variables (current process only)
os.environ["MY_APP_DEBUG"] = "true"
os.environ["MY_APP_PORT"] = "8080"

print(f"Debug: {os.getenv('MY_APP_DEBUG')}")  # true
print(f"Port: {os.getenv('MY_APP_PORT')}")  # 8080

# Checking if an env var exists
if "MY_APP_DEBUG" in os.environ:
    print("Debug mode is configured")  # Debug mode is configured

# Deleting an env var
del os.environ["MY_APP_DEBUG"]
print(f"Debug after delete: {os.getenv('MY_APP_DEBUG')}")  # None

# Parsing environment variables with type conversion
def get_env_int(key, default=0):
    """Get an environment variable as an integer."""
    value = os.getenv(key)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default

def get_env_bool(key, default=False):
    """Get an environment variable as a boolean."""
    value = os.getenv(key)
    if value is None:
        return default
    return value.lower() in ("true", "1", "yes", "on")

def get_env_list(key, separator=",", default=None):
    """Get an environment variable as a list."""
    value = os.getenv(key)
    if value is None:
        return default or []
    return value.split(separator)

os.environ["MY_PORT"] = "9090"
os.environ["MY_DEBUG"] = "true"
os.environ["MY_HOSTS"] = "host1,host2,host3"

print(f"Port (int): {get_env_int('MY_PORT')}")  # 9090
print(f"Debug (bool): {get_env_bool('MY_DEBUG')}")  # True
print(f"Hosts (list): {get_env_list('MY_HOSTS')}")  # ['host1', 'host2', 'host3']
print(f"Missing (int): {get_env_int('MISSING', 42)}")  # 42

print("=" * 5, "Configuration file (.ini format)", "=" * 5)

import configparser

config_path = os.path.join(EXAMPLE_DIR, "config.ini")

# Creating a configuration file
config = configparser.ConfigParser()

config["DEFAULT"] = {
    "debug": "false",
    "log_level": "INFO",
}

config["server"] = {
    "host": "localhost",
    "port": "8080",
    "debug": "true",
}

config["database"] = {
    "host": "db.example.com",
    "port": "5432",
    "name": "myapp_db",
    "user": "admin",
}

with open(config_path, "w") as f:
    config.write(f)

# Read back the config file
print(f"Config file contents:")
with open(config_path, "r") as f:
    print(f.read())

# Reading a configuration file
config2 = configparser.ConfigParser()
config2.read(config_path)

# Access sections and values
print(f"Server host: {config2['server']['host']}")  # localhost
print(f"Server port: {config2['server'].getint('port')}")  # 8080 (as int)
print(f"Server debug: {config2['server'].getboolean('debug')}")  # True (as bool)
print(f"DB name: {config2['database']['name']}")  # myapp_db

# DEFAULT values are inherited by all sections
print(f"Server log_level: {config2['server']['log_level']}")  # INFO (from DEFAULT)

# Listing sections
print(f"Sections: {config2.sections()}")  # ['server', 'database']

# Check if section/option exists
print(f"Has server: {'server' in config2}")  # True
print(f"Has cache section: {'cache' in config2}")  # False
print(f"Has server.host: {config2.has_option('server', 'host')}")  # True

# Get with fallback
print(f"Missing key: {config2.get('server', 'missing', fallback='default_value')}")  # default_value

print("=" * 5, "Configuration file (.toml format, Python 3.11+)", "=" * 5)

try:
    import tomllib  # Python 3.11+
except ImportError:
    import tomli as tomllib  # pip install tomli for Python < 3.11

toml_path = os.path.join(EXAMPLE_DIR, "config.toml")

# Creating a TOML config file
toml_content = """\
[server]
host = "localhost"
port = 8080
debug = true

[database]
host = "db.example.com"
port = 5432
name = "myapp_db"

[logging]
level = "INFO"
file = "app.log"
"""

with open(toml_path, "w") as f:
    f.write(toml_content)

# Reading a TOML file
with open(toml_path, "rb") as f:
    toml_config = tomllib.load(f)

print(f"Server host: {toml_config['server']['host']}")  # localhost
print(f"Server port: {toml_config['server']['port']}")  # 8080
print(f"Server debug: {toml_config['server']['debug']}")  # True
print(f"Database: {toml_config['database']}")  # {'host': 'db.example.com', ...}

print("=" * 5, "Configuration file (.json format)", "=" * 5)

import json

json_config_path = os.path.join(EXAMPLE_DIR, "config.json")

# Creating a JSON config file
json_config = {
    "server": {
        "host": "localhost",
        "port": 8080,
        "debug": True,
    },
    "database": {
        "host": "db.example.com",
        "port": 5432,
        "name": "myapp_db",
        "credentials": {
            "user": "admin",
            "password": "secret",
        },
    },
    "logging": {
        "level": "INFO",
        "file": "app.log",
    },
}

with open(json_config_path, "w") as f:
    json.dump(json_config, f, indent=2)

# Reading a JSON config file
with open(json_config_path, "r") as f:
    loaded_config = json.load(f)

print(f"Server: {loaded_config['server']}")  # {'host': 'localhost', 'port': 8080, 'debug': True}
print(f"DB user: {loaded_config['database']['credentials']['user']}")  # admin

# Accessing nested values safely with get()
db = loaded_config.get("database", {})
print(f"DB host: {db.get('host', 'localhost')}")  # db.example.com
print(f"DB missing: {db.get('missing', 'default')}")  # default