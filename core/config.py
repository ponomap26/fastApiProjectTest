from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///shop.sqlite3"
    # db_echo: bool= False
    db_echo: bool= True
settings = Settings()
