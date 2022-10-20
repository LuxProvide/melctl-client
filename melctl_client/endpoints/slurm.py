import os
from pathlib import Path

from .. import utils
from .__base__ import SimpleEndpoint, Endpoint


class JobSubmit(Endpoint):
    """Submits a Slurm batch job.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'submit')
        self.parser.add_argument('file', type=str, help='Batch file')
        self.parser.add_argument('--chdir', type=str, required=False, default='', help='Job working directory')

    def target(self, args):
        with open(str(Path(args.file).expanduser().absolute()), 'r') as fd:
            req = self.session.post(
                f'{self.url}/slurm/jobs',
                json={
                    'script': fd.read(),
                    'cwd': args.chdir
                }
            )
            req.raise_for_status()
            return req.json()


class JobList(Endpoint):
    """Lists Slurm jobs.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'list-jobs', headers=[
            'user_name', 'account', 'job_id', 'name', 'job_state'
        ])
        self.parser.add_argument('--user', type=str, required=False, default=None, help='User name')
        self.parser.add_argument('--account', type=str, required=False, default=None, help='Account name')

    def target(self, args):
        # Select endpoints
        if args.user:
            url = f'{self.url}/slurm/jobs/_/users/{args.user}'
        elif args.account:
            url = f'{self.url}/slurm/jobs/_/accounts/{args.user}'
        else:
            url = f'{self.url}/slurm/jobs'
        # Run
        req = self.session.get(
            url,
        )
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        return data.get('jobs', [])


class JobGet(Endpoint):
    """Gets one or more Slurm job.
    """

    def __init__(self, subparser):
        super().__init__(subparser, 'get-job', headers=[
            'user_name', 'account', 'job_id', 'name', 'job_state'
        ])
        self.parser.add_argument('ref', type=str, help='Slurm job reference (ID or name)')

    def target(self, args):
        req = self.session.get(
            f'{self.url}/slurm/jobs/{args.ref}',
        )
        req.raise_for_status()
        return req.json()

    def render(self, args, data):
        return data.get('jobs', [])
