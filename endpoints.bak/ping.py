from .__base__ import SimpleEndpoint


class Ping(SimpleEndpoint):
    """Test connection to MelCtl API server.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'ping', 'GET', 'ping?seconds={seconds}', wait=False)
        self.parser.add_argument('-s', '--seconds', dest='seconds', type=int,
            default=0, help='Ping time')
