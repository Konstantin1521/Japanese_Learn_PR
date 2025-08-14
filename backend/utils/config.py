import os

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


load_dotenv()


class RunConfig(BaseModel):
    host: str = '127.0.0.1'
    port: int = 8080
    reload: bool = True

class APIV1Prefix(BaseModel):
    prefix: str = '/api/v1'

class DatabaseConfig(BaseModel):
    url: str = os.getenv('DB_URL')
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

class KanaConfig(BaseModel):
    hg: str = "hiragana"
    kk: str = "katakana"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIV1Prefix = APIV1Prefix()
    kana: KanaConfig = KanaConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()
