import argparse

# Disable Pydantic warnings
import warnings

warnings.filterwarnings('ignore')

from .endpoints import endpoints
from .hints import Hinter


def load_endpoints(subparser):
    """Loads and initializes MelCtl endpoints.

    :param subparser: Argparse's subparser.
    """
    # Endpoints parsers, subparsers and instances
    endpoints_parsers = []
    endpoints_subparsers = []
    endpoints_instances = []
    # Endpoints parsers, subparsers and instances initialization
    for endpoint_name, endpoints_actions in endpoints.items():
        # For endpoint in form 'melctl <endpoint> <action> ...':
        if isinstance(endpoints_actions, (list, tuple, set)):
            endpoints_parsers.append(subparser.add_parser(endpoint_name))
            endpoints_subparsers.append(
                endpoints_parsers[-1].add_subparsers(dest='action')
            )
            for endpoint_action in endpoints_actions:
                endpoints_instances.append(endpoint_action(endpoints_subparsers[-1]))
                endpoints_subparsers[-1].required = True
        # For endpoint in form 'melctl <endpoint> ...':
        else:
            endpoints_instances.append(endpoints_actions(subparser))
    # Done
    return endpoints_parsers, endpoints_subparsers, endpoints_instances


class API:
    """Simple Python API wrapper.
    """

    def __init__(self, blocking: bool = True):
        # Args override
        self.args = {
            'outform': 'raw',
            'wait': blocking
        }
        # Root parser and subparser
        self.parser = argparse.ArgumentParser('melctl')
        self.subparser = self.parser.add_subparsers(dest='endpoint')
        self.subparser.required = True
        # Load and init endpoints
        _, _, self.endpoints = load_endpoints(self.subparser)

    def __call__(self, endpoint, *args):
        # Parse
        args = self.parser.parse_args(args=[endpoint, ] + list(args))
        # Update args
        for k, v in self.args.items():
            setattr(args, k, v)
        # Run
        return args.func(args)


def main():
    """MelCtl entry point.
    """
    # Root parser and subparser
    parser = argparse.ArgumentParser('melctl')
    subparser = parser.add_subparsers(dest='endpoint')
    subparser.required = True
    # Load and init endpoints
    endpoints_parsers, endpoints_subparsers, endpoints_instances = load_endpoints(subparser)
    # Parse arguments, run hints and invoke endpoint
    args = parser.parse_args()
    Hinter()(args)
    args.func(args)


if __name__ == '__main__':
    main()
