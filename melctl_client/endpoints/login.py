from datetime import datetime
import getpass
from jose import jwt
from pathlib import Path

from ..config import settings
from .__base__ import Endpoint


class User(Endpoint):
    """Login as user and obtain a token.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'user')

    def target(self, args):
        # Get user credentials
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        print()
        # Request token
        req = self.session.post(
            f'{args.url}/auth/oauth2/ldap',
            data={
                'username': username,
                'password': password,
                'grant_type': 'password'
            },
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )
        req.raise_for_status()
        # Extract token content
        token_data = req.json().get('access_token')
        token_path = Path(settings.Config.secrets_dir, 'token')
        # Create secrets dir and save token
        Path(settings.Config.secrets_dir).mkdir(parents=True, exist_ok=True)
        with open(token_path, 'w') as fd:
            fd.write(token_data)
        # Done
        return {
            'path': token_path,
            'status': 'Token updated'
        }


class Admin(Endpoint):
    """Login as API server admin and obtain a token.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'admin')
        self.parser.add_argument('user', type=str, help='User name')
        self.parser.add_argument('profile', type=str, help='User profile')
        self.parser.add_argument('validity', type=int, help='Token validity in seconds')
        self.parser.add_argument('-p', '--password', required=True, type=str, help='API password')
    
    def target(self, args):
        req = self.session.post(
            f'{args.url}/auth/oauth2/admin',
            data={
                'username': f'{args.user}:{args.profile}:{args.validity}',
                'password': args.password,
                'grant_type': 'password'
            },
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        )
        req.raise_for_status()
        return req.json()


class Info(Endpoint):
    """Get login info.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'info')
    
    def target(self, args):
        claims = jwt.get_unverified_claims(args.auth)
        claims.update({
            'valid_until_text': str(datetime.fromtimestamp(claims['valid_until']))
        })
        return claims
