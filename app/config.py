# A config file for the app
from pathlib import Path

# main paths for the app and exact configurations for the app
CONFIG_FILE = Path(__file__).resolve()
APP_DIR = CONFIG_FILE.parent
PROJECT_ROOT = APP_DIR.parent

# paths for existing input data and clipboard
RAW_DATA_FILE = PROJECT_ROOT / "input" / "sintetic_raw_dataset.csv"
BUMPER_DIR = PROJECT_ROOT / "bumper"