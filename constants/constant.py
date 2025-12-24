from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

print("Base_dir : ",BASE_DIR)


APP_NAME="app"
LOG_LEVEL="INFO"
LOG_FILE= BASE_DIR / "logs/log_data.logs"
LOG_MAX_SIZE=10485760
LOG_BACKUP_COUNT=5
LOG_FORMAT="%(asctime)s - %(name)s -%(levelname)s - %(message)s"
APP_ENV = None









