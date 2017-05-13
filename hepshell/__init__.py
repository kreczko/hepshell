from __future__ import absolute_import
import os
import sys
import logging

from . import settings as SETTINGS
from . import command
from . import interpreter

__version__ = '0.1.6'

if 'HEP_PROJECT_ROOT' not in os.environ:
    print("Could not find environmental variable 'HEP_PROJECT_ROOT'")
    print("You need to run 'source bin/env.sh' first!")
    sys.exit(-1)
HEP_PROJECT_ROOT = os.environ['HEP_PROJECT_ROOT']

HEP_PATH = os.path.dirname(__file__)
HEP_PATH = os.path.join(HEP_PATH, '..')

LOG = logging.getLogger('hepshell')
LOG.setLevel(logging.DEBUG)
# logging to a file
formatter = logging.Formatter(
    '%(asctime)s [%(name)s]  %(levelname)s: %(message)s')

logfile = '/tmp/hepshell_{0}.log'.format(os.geteuid())
if os.path.exists(HEP_PROJECT_ROOT + '/workspace/log'):
    logfile = HEP_PROJECT_ROOT + '/workspace/log/hepshell.log'
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
LOG.addHandler(fh)

# logging to the console
formatter = logging.Formatter('%(message)s')
ch = logging.StreamHandler()
if not os.environ.get("DEBUG", False):
    ch.setLevel(logging.INFO)
else:
    ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
LOG.addHandler(ch)

Command = command.Command

run_cli = interpreter.run_cli
run_command = interpreter.run_command


__all__ = [
    'interpreter',
    'run_cli',
    'run_command',
    'SETTINGS',
    'Command',
]
