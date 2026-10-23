from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_uri_atlas: str = ""
    redis_url: str = "redis://localhost:6379"
    kill_switch_secret: str = ""


settings = Settings()