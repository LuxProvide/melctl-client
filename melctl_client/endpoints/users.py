from .__base__ import SimpleEndpoint, Endpoint


class List(SimpleEndpoint):
    """Lists users.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list', 'GET', 'users',
            headers=['name', 'uid', 'gid', 'preserved', 'expired'])
        self.parser.add_argument('--all', action='store_true', default=False, help='List all (+expired)')

    def render(self, args, data):
        users: list = []
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


class Create(SimpleEndpoint):
    """Create a new user.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'create', 'POST', 'users')
        self.parser.add_argument('--email', type=str.lower, required=True,
            help='Email address')
        self.parser.add_argument('--firstname', type=str, required=True,
            help='First name / given name')
        self.parser.add_argument('--lastname', type=str, required=True,
            help='Last name / family name / surname')
        self.parser.add_argument('--name', type=str, default=None,
            help='Account name (optional)')
        self.parser.add_argument('--phone', type=str, default=None,
            help='Phone number (optional)')
        self.parser.add_argument('--uid', type=int, default=None,
            help='Account UID (optional)')
        self.parser.add_argument('--gid', type=int, default=None,
            help='Account GID (optional)')

    def target(self, args):
        # Required fields
        jsdata = {
            'email': args.email,
            'firstname': args.firstname,
            'lastname': args.lastname,
        }
        # Optional field
        for field in ['name', 'phone', 'uid', 'gid']:
            if getattr(args, field, None) is not None:
                jsdata[field] = getattr(args, field)
        # Send request
        req = self.session.post(
            f'{self.url}/{self.urn}',
            json=jsdata
        )
        self.handle_status(args, req)
        return req.json()


class S3Status(SimpleEndpoint):
    """Gets an user S3 access.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 's3-status', 'GET', 'users/{name}/s3ds',
            headers=['tag', 'uuid', 'fs_paths', 'fs_uid'])
        self.parser.add_argument('name', help='User name')

    def render(self, args, data):
        return data.get('s3ds_accesskeys', [])


class S3Setup(SimpleEndpoint):
    """Sets an user S3 access.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 's3-setup', 'POST', 'users/{name}/s3ds',
            headers=['tag', 'uuid', 'fs_paths', 'fs_uid', 'secretkey', 'accesskey'])
        self.parser.add_argument('name', help='User name')
        self.parser.add_argument('--paths', nargs='+', default=[], help='Extra allowed paths')

    def target(self, args):
        req = self.session.post(
            f'{self.url}/users/{args.name}/s3ds',
            json={
                'extra_paths': args.paths
            }
        )
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        return data.get('s3ds_accesskeys', [])
