from .__base__ import SimpleEndpoint, Endpoint


class List(SimpleEndpoint):
    """Lists users.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list', 'GET', 'users',
            headers=['name', 'uid', 'gid', 'preserved', 'expired'])
        self.parser.add_argument('--all', action='store_true', default=False, help='List all (+expired)')

    def render(self, args, data):
        users: list[dict] = []
        # Apply filters
        for user in data.get('users', []):
            # Ignore expired users if --all not present
            if user.get('expired') is True and not args.all:
                pass
            else:
                users.append(user)
        # Done
        return users


class Get(SimpleEndpoint):
    """Lists a specific user.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'get', 'GET', 'users/{name}',
            headers=['name', 'uid', 'gid', 'preserved', 'expired'])
        self.parser.add_argument('name', help='User name')

    def render(self, args, data):
        return data.get('users', [])


class S3Status(SimpleEndpoint):
    """Gets an user S3 access.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 's3-status', 'GET', 'users/{name}/s3ds',
            headers=['tag', 'uuid', 'fspaths', 'fsuid'])
        self.parser.add_argument('name', help='User name')

    def render(self, args, data):
        return data.get('s3ds_accesskeys', [])


class S3Setup(SimpleEndpoint):
    """Sets an user S3 access.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 's3-setup', 'POST', 'users/{name}/s3ds',
            headers=['tag', 'uuid', 'fspaths', 'fsuid'])
        self.parser.add_argument('name', help='User name')

    def render(self, args, data):
        return data.get('s3ds_accesskeys', [])
