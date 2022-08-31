import os
import re
import sys

from .config import settings


class Hinter:
    """Base hinter class."""

    # Hint messages colors control codes
    level_colors = {
        "reset": "\033[0m",
        "info": "\033[32m",
        "warning": "\033[33m",
        "problem": "\033[31m",
    }

    def hint_files(self, args):
        """Check the configuration file."""
        if not os.path.isfile(settings.Config.env_file):
            yield (
                "warning",
                f'Configuration file "{settings.Config.env_file}" not found',
            )

    def hint_variables(self, args):
        """Check the configuration values."""
        rex_url = re.compile(r".*(127|localhost).*")
        # ---
        # URL format
        msg_url = (
            "warning",
            """URL (-u, --url or config's "url") should not point to localhost or 127.0.0.1""",
        )
        if len(args.url) > 0 and rex_url.match(args.url):
            yield msg_url
        elif len(args.url) < 1 and rex_url.match(settings.url):
            yield msg_url
        # ---
        # JWT content
        if len(args.auth) < 1 or len(settings.token) < 1:
            yield (
                "warning",
                """Token (-a, --auth or secret "token") does not look like a valid JWT""",
            )

    def print_hint(self, args, level, msg):
        """Print a hint."""
        if args.nocolor:
            print(f"{level.upper()}: {msg}", file=sys.stderr)
        else:
            print(
                f"{self.level_colors[level]}"
                f"{level.upper()}: {msg}"
                f'{self.level_colors["reset"]}',
                file=sys.stderr,
            )

    def __call__(self, args):
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
