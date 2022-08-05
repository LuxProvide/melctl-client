from .__base__ import SimpleEndpoint, Endpoint


class Ping(SimpleEndpoint):
    """Demonstrates MelCtl endpoint.
    """

    def __init__(self, subparser):
        """Initializes the endpoint.

        This SimpleEndpoint initialize its parent class with:
            - subparser: The command line parser
            - ``test``: The endpoint action name
            - ``GET``: The HTTP method to invoke
            - ``test/ping?data={data}``: The URL fragment to template and invoke
        """
        super().__init__(subparser, 'ping', 'GET', 'test/ping?data={data}')
        self.parser.add_argument('-d', '--data', dest='data', type=str,
            default=None, help='Test ping data')


class Callback(Endpoint):
    """Demonstrates MelCtl callback endpoint.
    """

    hint_callback_url: str = '<MelCtl host>/test/callback/receive'

    def __init__(self, subparser):
        """Initializes the endpoint.

        This Endpoint initialize its parent class with:
            - subparser: The command line parser
            - ``callback``: The endpoint action name
        """
        super().__init__(subparser, 'callback')
        self.parser.add_argument('cback_url', type=str,
            help=f'Callback URL (you may try "{self.hint_callback_url}")')
        self.parser.add_argument('-m', '--method', dest='method', type=str.upper,
            default='POST', help='Callback HTTP method')

    def target(self, args):
        """Runs the endpoint.

        An ``Endpoint`` must implement a ``target`` method to call the API server.
        Parsed arguments are made available in ``args``.
        """
        req = self.session.get(
            f'{self.url}/test/callback/send'
            f'?url={args.cback_url}'
            f'&method={args.method}'
        )
        req.raise_for_status()
        return req.json()
