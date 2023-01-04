from . import ping
from . import version


commands = {
    'ping': ping.Ping,
    'version': version.Version
}
