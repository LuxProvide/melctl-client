import os

from ..config import settings
from .__base__ import Endpoint


class Show(Endpoint):
    """Shows client configuration.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'show')
    
    def target(self, args):
        conf = dict([(k, v) for k, v in settings])
        conf['env_file'] = settings.Config.env_file
        conf['secrets_dir'] = settings.Config.secrets_dir
        return conf


class Init(Endpoint):
    """Creates a new, default configuration
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'init')
    
    def target(self, args):
        results = [{}]
        # ---
        # Configuration file
        results.append({'path': settings.Config.env_file})
        if not os.path.exists(settings.Config.env_file):
            with open(settings.Config.env_file, 'w') as fd:
                for k, v in settings:
                    if isinstance(v, (int, float)):
                        fd.write(f'{k}={v}')
                    elif isinstance(v, str):
                        fd.write(f'{k}="{v}"')
                    fd.write(os.linesep)
            results[-1]['status'] = 'File created'
        else:
            results[-1]['status'] = 'File already exists, no change made'
        # ---
        # Secrets directory
        results.append({'path': settings.Config.secrets_dir})
        if not os.path.isdir(settings.Config.secrets_dir):
            os.mkdir(settings.Config.secrets_dir)
            results[-1]['status'] = 'Directory created'
        else:
            results[-1]['status'] = 'Directory already exists, not change made'
        # ---
        return results
