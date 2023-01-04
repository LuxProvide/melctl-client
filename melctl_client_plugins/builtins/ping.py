from melctl_client.commands import SimpleCommand


class Ping(SimpleCommand):
    def __init__(self, subparser):
        super().__init__(subparser, 'ping', 'GET', 'ping?seconds={seconds}', wait=False)
        self.parser.add_argument('-s', '--seconds', dest='seconds', type=int,
            default=0, help='Ping time')
