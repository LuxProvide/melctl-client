import re

from melctl_client import __version__
from melctl_client.commands import Command


class Version(Command):
    """Show MelCtl server and client versions.
    """

    rex = re.compile(r'(?P<major>[0-9]+)\.(?P<minor>[0-9]+)\.(?P<patch>[0-9]+)')

    def __init__(self, subparser):
        super().__init__(subparser, 'version')
        self.parser.add_argument('mode', choices=['client', 'server'],
            nargs='?', default=None, help='Show only client or server version')

    def target(self, args):
        if args.mode in [None, 'server']:
            req = self.session.get(f'{self.url}/version')
            req.raise_for_status()
            return req.json()
        else:
            return {}

    def render(self, args, data):
        # ---
        # Insert client version
        if args.mode in [None, 'client']:
            data['clientVersion'] = __version__
        # ---
        # Parse server and client version
        match_server = self.rex.match(data.get('serverVersion', '0.0.0'))
        match_client = self.rex.match(data.get('clientVersion', '0.0.0'))
        # ---
        # Generate message
        if args.mode in [None, 'server'] and match_server and match_client:
            # Warning - Major version should match
            if int(match_server.group('major')) != int(match_client.group('major')):
                data['info'] = 'Warning: major versions differs'
        # ---
        # Default message
        if not 'info' in data:
            data['info'] = 'OK'
        # ---
        # Done
        return data
