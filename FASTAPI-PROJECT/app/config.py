import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent


def get_secret(
        key: str,
        default_value: Optional[str] = None,
        json_path: str = str(BASE_DIR / "secret.json")
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"set th {key} environment variables.")


POSTGRES_DB_NAME = get_secret("db")
POSTGRES_DB_HOST = get_secret("host")
POSTGRES_DB_PORT = get_secret("port")
POSTGRES_DB_USER = get_secret("user")
POSTGRES_DB_PASSWORD = get_secret("password")
NAVER_API_ID = get_secret("naver_api_id")
NAVER_API_SECRET = get_secret("naver_api_secret")

if __name__ == "__main__":
    word = get_secret("hello")
    print(word)
