import re
import json

from .__base__ import Endpoint, SimpleEndpoint


class List(Endpoint):
    """Lists defined tasks.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list')
    
    def target(self, args):
        req = self.session.get(f'{self.url}/tasks')
        req.raise_for_status()
        return [{'task': task} for task in req.json().get('tasks', [])]


class Queued(SimpleEndpoint):
    """Lists queued tasks.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'queued', 'GET', 'tasks/queued',
            headers=['id', 'name', 'schedule'])


class Status(SimpleEndpoint):
    """Returns a tasks status.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'status', 'GET', 'tasks/status/{task_id}')
        self.parser.add_argument('task_id', type=str, help='Task ID')


class Get(SimpleEndpoint):
    """Returns a task output.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'get', 'GET', 'tasks/results/{task_id}')
        self.parser.add_argument('task_id', type=str, help='Task ID')


class Submit(Endpoint):
    """Submits (creates) a new task.
    """

    @staticmethod
    def str_to_bool(value: str) -> bool:
        return value.lower() in ['true', 'yes', '1']

    re_argcast = re.compile(r'(?P<cast>(int|float|bool)):(?P<value>.*)')
    casts = {
        'int': int,
        'float': float,
        'bool': str_to_bool
    }

    def __init__(self, subparser):
        super().__init__(subparser, 'submit', wait=False)
        self.parser.add_argument('name', type=str, help='Task name')
        self.parser.add_argument('--args', nargs='+', default=[],
            help=f'''
            Task arguments where ARGS is <value> or <type>:<value> 
            and <type> is one of {', '.join(self.casts.keys())}
            ''')
        self.parser.add_argument('--kwargs', type=str, default=None,
            help='Task keyword arguments as a JSON string')

    def target(self, args):
        # Cast positional arguments
        _args = []
        for arg in args.args:
            match = self.re_argcast.match(arg)
            if match:
                cast = self.casts[match.group('cast')]
                value = match.group('value')
                _args.append(cast(value))
            else:
                _args.append(arg)
        # Generate keyword arguments
        _kwargs = {}
        if args.kwargs is not None:
            _kwargs = json.loads(args.kwargs)
        # Process
        req = self.session.post(
            f'{self.url}/tasks/submit',
            json={
                'name': args.name,
                'args': _args,
                'kwargs': _kwargs
            })
        # Done
        req.raise_for_status()
        return req.json()
