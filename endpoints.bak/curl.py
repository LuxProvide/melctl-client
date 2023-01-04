import json
from .__base__ import Endpoint


class Curl(Endpoint):
    """Generic call to a MelCtl API endpoint.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'curl')
        self.parser.add_argument('method', type=str.lower, help='API method')
        self.parser.add_argument('endpoint', type=str, help='API path')
        self.parser.add_argument('-j', '--json', dest='json', type=str,
            default='{}', help='JSON payload (POST only')

    def target(self, args):
        url = f'{self.url}/{args.endpoint.strip("/")}'
        if args.method == 'get':
            req = self.session.get(url)
        elif args.method == 'post':
            req = self.session.post(url, json=json.loads(args.json))
        req.raise_for_status()
        return req.json()
