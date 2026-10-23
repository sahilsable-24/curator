from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(from_attributes=True)

    mongodb_uri: str = ""
    redis_url: str = "redis://localhost:6379"
    kill_switch_secret: str = ""\


settings = Settings()