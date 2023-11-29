from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Build System'
    app_description: str = (
        'Service for creating build systems',
        'that automates and speeds up routine processes'
    )

    class Config:
        env_file = '.env'


settings = Settings()
