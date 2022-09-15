import os
import re
import sys

from argparse import Namespace

from .config import settings


class Hinter:
    """Base hinter class."""

    # Hint messages colors control codes
    level_colors: dict[str, str] = {
        "reset": "\033[0m",
        "info": "\033[32m",
        "warning": "\033[33m",
        "problem": "\033[31m",
    }

    # Regex to match localhost
    localhost_rex: re.Pattern = re.compile(r'.*(127|localhost).*')

    def hint_files(self, args: Namespace):
        """Check the configuration file."""
        if not os.path.isfile(settings.Config.env_file):
            yield (
                "warning",
                f'Configuration file "{settings.Config.env_file}" not found',
            )

    def hint_variables(self, args: Namespace):
        """Check the configuration values."""
        # URL format
        msg_url = (
            "warning",
            """URL (-u, --url or config's "url") should not point to localhost or 127.0.0.1""",
        )
        if len(args.url) > 0 and self.localhost_rex.match(args.url):
            yield msg_url
        elif len(args.url) < 1 and self.localhost_rex.match(settings.url):
            yield msg_url
        # JWT content
        if len(args.auth) < 1 or len(settings.token) < 1:
            yield (
                "warning",
                """Token (-a, --auth or secret "token") does not look like a valid JWT""",
            )

    def print_hint(self, args: Namespace, level: str, msg: str):
        """Print a hint.

        :param level Hint level:
        :param msg: Hint content
        """
        if args.nocolor:
            print(f"{level.upper()}: {msg}", file=sys.stderr)
        else:
            print(
                f"{self.level_colors[level]}"
                f"{level.upper()}: {msg}"
                f'{self.level_colors["reset"]}',
                file=sys.stderr,
            )

    def __call__(self, args: Namespace):
        """Run all hints.

        :param args: Parsed arguments.
        """
        _hinted = False
        for hinter in [
            self.hint_files,
            self.hint_variables,
        ]:
            try:
                for level, msg in hinter(args):
                    _hinted = True
                    self.print_hint(args, level, msg)
            except Exception as error:
                _hinted = True
                self.print_hint(
                    args,
                    "problem",
                    f"Failed to run hinter {hinter.__name__}: {str(error)}",
                )
                if args.traceback:
                    self.print_hint(
                        args, "problem", "Dumping exception as -t|--traceback is set"
                    )
                    raise
        if _hinted:
            print("", file=sys.stderr)
