import os
from pathlib import Path
from pydantic import BaseSettings


class Settings(BaseSettings):
    """MelCTL settings.

    :param url: MelCTL URL
    :param token: MelCTL API token
    """

    # MelCtl server URL
    url: str = 'http://127.0.0.1:8888'

    # MelCtl authentication token
    token: str = ''

    class Config:
        """Configuration source.
        """

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
