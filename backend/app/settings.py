from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Database
    DATABASE_URL: str | None = None

    # Payments
    STRIPE_SECRET_KEY: str | None = None

    # Auth (shared with auth-microservice if you want SSO)
    JWT_SECRET: str = Field(default="dev-secret-change-me")

    # CORS
    # Comma-separated list of allowed origins
    # Example: https://ecommerce-ui-5hvm.onrender.com
    CORS_ORIGINS: str = "*"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        case_sensitive=False,
    )

settings = Settings()

