import sys

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
        super().__init__(subparser, 'get', headers=['name', 'users', 'coordinators', 'info'])
        self.parser.add_argument('project', nargs='+',
            help='Project(s) name or path')

    def target(self, args):
        req = self.session.get(f'{self.url}/projects')
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        return [
            account for account in data.get('projects', [])
            if account.get('name', '') in args.project
        ]


class Create(Endpoint):
    """Creates a new project.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'create')
        self.parser.add_argument('name', type=str, help='Project name')
        self.parser.add_argument('--uid', type=int, default=-1, help='Project UID')
        self.parser.add_argument('--parent', type=str, help='Parent project name', default='')

    def target(self, args):
        # Project definition
        jsdata = {
            'name': args.name,
            'uid': args.uid,
            'parent': args.parent
        }
        # Run
        req = self.session.post(f'{self.url}/projects', json=jsdata)
        req.raise_for_status()
        return req.json()


class Setup(Endpoint):
    """Configures a project.
    """

    tres = ('cpu', 'gpu', 'mem', 'fpga')

    def __init__(self, subparser):
        super().__init__(subparser, 'setup')
        self.parser.add_argument('name', type=str, help='Project name')
        for tres in self.tres:
            self.parser.add_argument(f'--{tres}', dest=f'{tres}_mins', type=int, default=-1, help=f'{tres.upper()} quota in minutes')

    def target(self, args):
        # Project definition
        jsdata = {}
        # Project quotas
        for tres in self.tres:
            jsdata[f'{tres}_mins'] = getattr(args, f'{tres}_mins')
        # Run
        req = self.session.post(f'{self.url}/projects/{args.name}/setup', json=jsdata)
        req.raise_for_status()
        return req.json()


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
            url = f'{self.url}/projects'
            params['names'] = ','.join(args.projects)
        else:
            url = f'{self.url}/projects'
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
