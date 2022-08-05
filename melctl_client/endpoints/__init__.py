import sys
from textwrap import dedent

from .. import __version__


# Import endpoints modules
try:
    from . import ping
    from . import version
    from . import login
    from . import conf
    # from . import test
    from . import tasks
    from . import projects
    from . import curl
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
    # 'test': [
    #     test.Ping,
    #     test.Callback
    # ],
    'projects': [
        projects.Projects,
        projects.Get,
        projects.Create,
        projects.Setup,
        projects.Report
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
