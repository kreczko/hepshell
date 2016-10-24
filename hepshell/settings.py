import os
import logging

LOG = logging.getLogger(__name__)

'''
    List of modules which should be loaded as commands for hepshell
'''
COMMANDS = [
    'hepshell.commands'
]

# load ENV variables as settings if available
ENV_PREFIX = 'HEPSHELL_'
for key in os.environ:
    if key.startswith(ENV_PREFIX):
        name = key[len(ENV_PREFIX):].upper()
        globals()[name] = os.environ[key]

# if hepshell_settings exists in PYTHONPATH import all definitions
try:
    from hepshell_settings import *
except ImportError:
    LOG.warning('Could not locate hepshell settings')
    pass
    
