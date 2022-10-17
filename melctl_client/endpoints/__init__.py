import sys
from textwrap import dedent

from .. import __version__


# Import endpoints modules
try:
    from . import ping
    from . import version
    from . import login
    from . import conf
    from . import tasks
    from . import projects
    from . import curl
    from . import s3ds
    from . import users
except Exception:
    errmsg = dedent(f'''\
        Error while importing endpoints modules

        Please report the issue with the following details.

        ---------------------------------------------------

        melctl_client version:
          {__version__}
    ''')
    print(errmsg, file=sys.stderr)
    raise


# Register endpoints modules and actions
endpoints = {
    'ping': ping.Ping,
    'version': version.Version,
    'login': [
        login.User,
        login.Admin,
        login.Info
    ],
    'config': [
        conf.Show,
        conf.Init
    ],
    'projects': [
        projects.Projects,
        projects.Get,
        projects.Create,
        projects.Setup,
        projects.Report
    ],
    'users': [
        users.List,
        users.Get,
        users.S3Status,
        users.S3Setup
    ],
    's3ds': [
        s3ds.List,
        s3ds.Setup,
        s3ds.Disable
    ],
    'tasks': [
        tasks.List,
        tasks.Queued,
        tasks.Status,
        tasks.Get,
        tasks.Submit
    ],
    'curl': curl.Curl
}
