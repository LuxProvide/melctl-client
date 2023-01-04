import sys
from textwrap import dedent

from .. import utils
from .__base__ import SimpleEndpoint, Endpoint


class Projects(SimpleEndpoint):
    """Lists queued tasks.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list', 'GET', 'projects',
            headers=['name', 'path', 'tres'])
    
    def render(self, args, data):
        return data.get('projects', [])


class Get(Endpoint):
    """List a single project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'get',
            headers=['name', 'path', 'tres'])
        # self.parser.add_argument('project', nargs='+',
        #     help='Project(s) name or path')
        self.parser.add_argument('project', type=str,
            help='Project name or path')

    def target(self, args):
        req = self.session.get(f'{self.url}/projects/{args.project}')
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        return data.get('projects', [])


class Create(Endpoint):
    """Creates a new project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'create')
        self.parser.add_argument('-p', '--parent', type=str,
            required=True, help='Parent project name')
        self.parser.add_argument('--name', type=str, default=None,
            help='Project name')
        self.parser.add_argument('--uid', type=int, default=-1,
            help='Project UID')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        # Auto create
        if (args.name, args.uid) == (None, -1):
            jsdata = {
                'parent': args.parent
            }
        # Manual creation
        elif args.name is not None and args.uid > 0:
            jsdata = {
                'parent': args.parent,
                'name': args.name,
                'uid': args.uid
            }
        # Invalid parameters
        else:
            print(
                '--name requires a valid project uid with --uid > 0',
                file=sys.stderr
            )
            print(
                '--uid must be > 0 and requires a valid project name with --name',
                file=sys.stderr
            )
            sys.exit(1)
        # Proceed
        req = self.session.post(f'{self.url}/projects', json=jsdata)
        req.raise_for_status()
        return req.json()


class AddSharedFS(Endpoint):
    """Add a SharedFS tier to a project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'add-sharedfs')
        self.parser.add_argument('name', type=str, help='Project name')
        self.parser.add_argument('--tier', type=int, required=True, choices=(1, 2), help='SharedFS tier')
        self.parser.add_argument('--owner', type=str, required=True, help='SharedFS directory owner (user name)')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        req = self.session.post(f'{self.url}/projects/{args.name}/sharedfs', json={
            'tier': args.tier,
            'owner': args.owner
        })
        req.raise_for_status()
        return req.json()


class SetQuotas(Endpoint):
    """Configures a project quotas.
    """

    compute_tres = ('cpu', 'gpu', 'mem', 'fpga')

    def __init__(self, subparser):
        super().__init__(subparser, 'set-quotas')
        # Project name
        self.parser.add_argument('name', type=str, help='Project name')
        # Compute quotas
        for tres in self.compute_tres:
            self.parser.add_argument(f'--{tres}', dest=f'{tres}_mins',
                type=int, default=-1, help=f'{tres.upper()} quota in minutes')
        # SharedFS quotas
        self.parser.add_argument('--tier', type=int, default=-1, choices=(1, 2), help='SharedFS tier')
        self.parser.add_argument('--kbytes', type=int, default=-1, help='SharedFS disk quotas in Kbytes')
        self.parser.add_argument('--inodes', type=int, default=-1, help='SharedFS inodes quotas')

    def target_compute(self, args):
        """Sets compute quotas (if any)
        """
        jsdata = {}
        # Prepare
        for tres in self.compute_tres:
            if getattr(args, f'{tres}_mins', -1) >= 0:
                jsdata[f'{tres}_mins'] = getattr(args, f'{tres}_mins')
        # Proceed
        if len(jsdata) > 0:
            req = self.session.post(
                f'{self.url}/projects/{args.name}/quotas/compute',
                json=jsdata
            )
            req.raise_for_status()
            return req.json()
        return {}

    def target_sharedfs(self, args):
        """Sets shared file system quotas (if any)
        """
        # Check if a SharedFS quota is being requested
        if args.tier > 0 or args.kbytes >= 0 or args.inodes >= 0:
            # Block invalid argument set
            if args.tier not in (1, 2) or args.kbytes < 0 or args.inodes < 0:
                print(
                    dedent('''\
                        --tier must be 1 or 2 and requires --kbytes and --inodes
                        --kbytes must be >= 0 and requires --tier and --inodes
                        --inodes must be >= 0 and requires --tier and --kbytes
                    '''),
                    file=sys.stderr
                )
                sys.exit(1)
            # Proceed
            req = self.session.post(
                f'{self.url}/projects/{args.name}/quotas/sharedfs',
                json={
                    'tier': args.tier,
                    'kbytes': args.kbytes,
                    'inodes': args.inodes
                }
            )
            req.raise_for_status()
            return req.json()
        return {}

    def target(self, args):
        result = {}
        for name, func in {
            'compute': self.target_compute,
            'sharedfs': self.target_sharedfs
        }.items():
            try:
                result[name] = func(args)
            except Exception as error:
                result[name] = str(error)
        return result


class Report(Endpoint):
    """Show a project usage report.
    """

    unit_time_factors = {
        's': 1,
        'm': 60,
        'h': 3600
    }

    def __init__(self, subparser):
        super().__init__(subparser, 'report',
            headers=['name', 'disk', 'cpu', 'gpu', 'mem', 'fpga', 'jobs'])
        # Project name
        self.parser.add_argument('projects', nargs='*')
        # Aggregation name
        self.parser.add_argument('--aggregate', type=str, default=None,
            help='Aggregation name')
        # Time range shortcut
        self.parser.add_argument('-r', '--rangetime', dest='time_range',
            type=str.lower, default=None, choices=['lastmonth',],
            help='Time range shortcut')
        # Time start
        self.parser.add_argument('-s', '--starttime', dest='time_start',
            required='-r' not in sys.argv and '--rangetime' not in sys.argv,
            type=str, default=None,
            help='Time range start as YYYY-MM-DD[T<HH:MM:SS>]')
        # Time end
        self.parser.add_argument('-e', '--endtime', dest='time_end',
            required='-r' not in sys.argv and '--rangetime' not in sys.argv,
            type=str, default=None,
            help='Time range end as YYYY-MM-DD[T<HH:MM:SS>]')
        # Time unit
        self.parser.add_argument('--time-unit', dest='unit_time',
            type=str.lower,
            default='s',
            choices=[
                's', 'sec', 'secs',  'second', 'seconds',
                'm', 'min', 'mins', 'minute', 'minutes',
                'h', 'hrs', 'hour', 'hours'
            ],
            help='Time unit')
        # Truncate
        self.parser.add_argument('--no-truncate', dest='truncate',
            action='store_false', default=True,
            help='Disable job truncation in time frame')

    def target(self, args):
        params = {
            'aggregate': args.aggregate,
            'truncate': args.truncate
        }
        # ---
        # Build URL
        if len(args.projects) == 1:
            url = f'{self.url}/projects/{args.projects[0]}'
        elif len(args.projects) > 1:
            url = f'{self.url}/projects/_'
            params['names'] = ','.join(args.projects)
        else:
            url = f'{self.url}/projects/_'
        # ---
        # Setup time range
        if args.time_range is not None:
            if args.time_range == 'lastmonth':
                args.time_start = utils.strftime_slurm(utils.last_month_som())
                args.time_end = utils.strftime_slurm(utils.last_month_eom())
        params.update({
            'time_start': args.time_start,
            'time_end': args.time_end,
        })
        # ---
        # Run request
        req = self.session.get(f'{url}/report', params=params)
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        accounts = []
        for account in data.get('accounts', []):
            accounts.append({
                'name': account.get('name'),
                'jobs': account.get('jobs')
            })
            # Partitions usage
            for alloc_name, alloc in account.get('usage', {}).items():
                if alloc_name in ['cpu', 'gpu', 'mem', 'fpga']:
                    accounts[-1].update({
                        alloc_name: int(alloc / self.unit_time_factors[args.unit_time[0]])
                    })
        return accounts


class AddUser(SimpleEndpoint):
    """Add user(s) to a project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'add-user', 'POST', 'projects/{project}/users')
        self.parser.add_argument('project', type=str, help='Project name')
        self.parser.add_argument('-m' ,'--members', type=str, nargs='+', default=[], help='List of user names')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        req = self.session.post(
            f'{self.url}/projects/{args.project}/users',
            json={
                'members': args.members
            }
        )
        self.handle_status(args, req)
        return req.json()


class AddCoordinator(SimpleEndpoint):
    """Add coordinator(s) to a project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'add-coord', 'POST', 'projects/{project}/coordinators')
        self.parser.add_argument('project', type=str, help='Project name')
        self.parser.add_argument('-m' ,'--members', type=str, nargs='+', default=[], help='List of coordinators names')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        req = self.session.post(
            f'{self.url}/projects/{args.project}/coordinators',
            json={
                'members': args.members
            }
        )
        self.handle_status(args, req)
        return req.json()


class DelUser(SimpleEndpoint):
    """Remove user(s) from a project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'del-user', 'DELETE', 'projects/{project}/users')
        self.parser.add_argument('project', type=str, help='Project name')
        self.parser.add_argument('-m' ,'--members', type=str, nargs='+', default=[], help='List of user names')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        req = self.session.delete(
            f'{self.url}/projects/{args.project}/users',
            json={
                'members': args.members
            }
        )
        self.handle_status(args, req)
        return req.json()


class DelCoordinator(SimpleEndpoint):
    """Remove coordinator(s) from a project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'del-coord', 'DELETE', 'projects/{project}/coordinators')
        self.parser.add_argument('project', type=str, help='Project name')
        self.parser.add_argument('-m' ,'--members', type=str, nargs='+', default=[], help='List of coordinators names')
        # Update default output format
        self.parser.set_defaults(outform='yaml')

    def target(self, args):
        req = self.session.delete(
            f'{self.url}/projects/{args.project}/coordinators',
            json={
                'members': args.members
            }
        )
        self.handle_status(args, req)
        return req.json()
