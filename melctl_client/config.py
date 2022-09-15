import os
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    """MelCTL setting structure.

    :param url: MelCTL URL
    :param token: MelCTL API token
    """

    url: str = 'http://127.0.0.1:8888'
    token: str = ''

    class Config:
        # Path to configuration file
        env_file = str(
            Path(os.environ.get('MELCTL_CLI_CONFIG', '~/.melctl-cli.env'))
            .expanduser()
            .absolute()
        )

        # Path to secrets directory
        secrets_dir = str(
            Path(os.environ.get('MELCTL_CLI_SECRETS', '~/.melctl-secrets'))
            .expanduser()
            .absolute()
        )


settings = Settings()
