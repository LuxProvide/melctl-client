from .. import utils
from .__base__ import SimpleEndpoint, Endpoint


class List(SimpleEndpoint):
    """Lists access keys.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list', 'GET', 's3ds/accesskeys',
            headers=['tag', 'uuid', ])
        self.parser.add_argument('--all', action='store_true', default=False, help='Include disabled keys')
    
    def render(self, args, data):
        keys_list = data.get('s3ds_accesskeys', [])
        if len(keys_list) and not args.all:
            return [
                k for k in keys_list
                if k.get('enabled', True)
            ]
        self.headers.append('enabled')
        return keys_list


class Setup(Endpoint):
    """Setup an user access key.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'setup')
        self.parser.add_argument('user', type=str, help='User name (== access key tag)')
        self.parser.add_argument('--uid', type=int, required=True, help='User UID')
        self.parser.add_argument('--gid', type=int, required=True, help='User GID')
        self.parser.add_argument('--paths', nargs='+', default=[], help='Allowed paths')

    def target(self, args):
        req = self.session.post(
            f'{self.url}/s3ds/accesskeys',
            json={
                'user': args.user,
                'fs_uid': args.uid,
                'fs_gid': args.gid,
                'fs_paths': args.paths
            }
        )
        req.raise_for_status()
        return req.json()


class Disable(Endpoint):
    """Disable / delete an access key.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'disable')
        self.parser.add_argument('user', type=str, help='User name (== access key tag)')
    
    def target(self, args):
        req = self.session.delete(f'{self.url}/s3ds/accesskeys/{args.user}')
        req.raise_for_status()
        return req.json()
