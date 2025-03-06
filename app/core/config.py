import os
from pydantic_settings import BaseSettings
from pydantic import Field, validator
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Diaflo_BEA"
    API_VERSION: str = "v1"

    # Database
    POSTGRES_USER: str = Field(default=os.getenv("POSTGRES_USER"))
    POSTGRES_PASSWORD: str = Field(default=os.getenv("POSTGRES_PASSWORD"))
    POSTGRES_DB: str = Field(default=os.getenv("POSTGRES_DB"))
    POSTGRES_HOST: str = Field(default=os.getenv("POSTGRES_HOST"))
    POSTGRES_PORT: int = Field(default=5432)

    # Redis
    REDIS_HOST: str = Field(default=os.getenv("REDIS_HOST"))
    REDIS_PORT: int = Field(default=6379)

    # Computed Fields
    DATABASE_URL: str = Field(default="")
    # CELERY_BROKER_URL: str = Field(default="")
    CELERY_BROKER_URL: str = f"redis://{os.getenv('REDIS_HOST')}:{os.getenv('REDIS_PORT')}/0"

    @validator("DATABASE_URL", pre=True, always=True)
    def assemble_db_url(cls, _, values):
        print("DATABASE_URL values:", values)
        if "POSTGRES_PORT" not in values:
            raise ValueError("POSTGRES_PORT missing")
        return (
            f"postgresql://{values['POSTGRES_USER']}:{values['POSTGRES_PASSWORD']}@"
            f"{values['POSTGRES_HOST']}:{values['POSTGRES_PORT']}/{values['POSTGRES_DB']}"
        )

    # @validator("CELERY_BROKER_URL", pre=True, always=True)
    # def assemble_celery_url(cls, _, values):
    #     print("CELERY_BROKER_URL", values)
    #     if "REDIS_PORT" not in values:
    #         raise ValueError("REDIS_PORT missing")
    #     return f"redis://{values['REDIS_HOST']}:{values['REDIS_PORT']}/0"

settings = Settings()

