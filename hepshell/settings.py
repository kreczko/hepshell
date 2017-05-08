import os
import logging
from collections import namedtuple

# List of modules which should be loaded as commands for hepshell
COMMANDS = [
    # 'hepshell.commands'
]
INTERPRETERS = namedtuple('Interpreters', ['CLICK_BASED', 'LEGACY'])(
    'CLICK_BASED', 'legacy')

#
INTERPRETER = INTERPRETERS.CLICK_BASED

LOG = {
    'name': 'hepshell',
    'logToFile': True,
    'logLevelFile': logging.DEBUG,
    'logFile': '/tmp/hepshell_{0}.log'.format(os.geteuid()),
    'logToConsole': True,
    'logLevelConsole': logging.INFO,
}

# load ENV variables as settings if available
ENV_PREFIX = 'HEPSHELL_'
for key in os.environ:
    if key.startswith(ENV_PREFIX):
        name = key[len(ENV_PREFIX):].upper()
        globals()[name] = os.environ[key]
