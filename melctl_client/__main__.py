import argparse

# Disable Pydantic warnings
import warnings

warnings.filterwarnings("ignore")

from .endpoints import endpoints
from .hints import Hinter


def main():
    """Entry point."""
    # Root parser and subparser
    parser = argparse.ArgumentParser("melctl")
    subparser = parser.add_subparsers(dest="endpoint")
    subparser.required = True
    # ---
    # Endpoints parsers, subparsers and instances
    endpoints_parsers = []
    endpoints_subparsers = []
    endpoints_instances = []
    # ---
    # Endpoints parsers, subparsers and instances initialization
    for endpoint_name, endpoints_actions in endpoints.items():
        # ---
        # For endpoint in form 'melctl <endpoint> <action> ...':
        if isinstance(endpoints_actions, (list, tuple, set)):
            endpoints_parsers.append(subparser.add_parser(endpoint_name))
            endpoints_subparsers.append(
                endpoints_parsers[-1].add_subparsers(dest="action")
            )
            for endpoint_action in endpoints_actions:
                endpoints_instances.append(endpoint_action(endpoints_subparsers[-1]))
                endpoints_subparsers[-1].required = True
        # ---
        # For endpoint in form 'melctl <endpoint> ...':
        else:
            endpoints_instances.append(endpoints_actions(subparser))
    # ---
    # Parse arguments, run hints and invoke endpoint
    args = parser.parse_args()
    Hinter()(args)
    args.func(args)


if __name__ == "__main__":
    main()
