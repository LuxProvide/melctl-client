import importlib
import pkgutil
import argparse

# Disable Pydantic warnings
import warnings
warnings.filterwarnings('ignore')

# MelCtl plugins packages
import melctl_client_plugins

from .hints import Hinter


def load_commands(commands, subparser):
    """Loads and initializes MelCtl commands.

    :param subparser: Argparse's subparser
    """
    # Commands parsers, subparsers and instances
    commands_parsers = []
    commands_subparsers = []
    commands_instances = []
    # Commands parsers, subparsers and instances initialization
    for command_name, commands_actions in commands.items():
        # For command in form 'melctl <command> <action> ...':
        if isinstance(commands_actions, (list, tuple, set)):
            commands_parsers.append(subparser.add_parser(command_name))
            commands_subparsers.append(
                commands_parsers[-1].add_subparsers(dest='action')
            )
            for command_action in commands_actions:
                commands_instances.append(command_action(commands_subparsers[-1]))
                commands_subparsers[-1].required = True
        # For command in form 'melctl <command> ...':
        else:
            commands_instances.append(commands_actions(subparser))
    # Done
    return commands_parsers, commands_subparsers, commands_instances


def load_plugins(subparser, pkgs: list = [melctl_client_plugins,]):
    """Load MelCtl client plugins.

    :param subparser: Argparse's subparser
    :param pkgs: Packages to load plugins from
    """
    for pkg in pkgs:
        for _, name, _ in pkgutil.iter_modules(pkg.__path__, pkg.__name__ + '.'):
            # Import plugin
            plugin = importlib.import_module(name)
            # Load plugin commands
            if hasattr(plugin, 'commands'):
                load_commands(plugin.commands, subparser)


def main():
    """MelCtl entry point.
    """
    # Root parser and subparser
    parser = argparse.ArgumentParser('melctl')
    subparser = parser.add_subparsers(dest='command')
    subparser.required = True
    # Load and init plugins & commands
    load_plugins(subparser)
    # Parse arguments, run hints and invoke command
    args = parser.parse_args()
    Hinter()(args)
    args.func(args)


if __name__ == '__main__':
    main()
