# hepshell

[![Build Status](https://travis-ci.org/kreczko/hepshell.svg?branch=master)](https://travis-ci.org/kreczko/hepshell)

A Python Shell for High Energy Particle Physics.
hepshell is meant as a starting point for creating your own analysis shell.
It provides auto-completion (in shell mode), command execution and a few basic
commands such as printing help or creating & checking your grid proxy.



# Setup

A typical HEPSHELL project is expected to have the following minimal folder structure:
 - bin (all scripts/executables)
 - python (all python modules & packages)

In your `{project}/bin` directory add a python script with the following content
from `examples/cli-ex` and make it executable `chmod a+x <the script>`.
The name of the file will be used as the prompt prefix for your custom shell
.
Furthermore one should add `{project}/bin/env.sh` which sets up the environment.
At the very least this shell script should define `HEP_PROJECT_ROOT` and update
the `PATH` and `PYTHONPATH` variables (see `examples/env-minimal.sh`)


# running commands
Once you have your project set up you can run commands via
```bash
<your hepshell alias> <command>
```
In order to enable debug information simply prepend `DEBUG=1` before any command
or execute `export DEBUG=1` once.

To use the completion feature of the hepshell you need to enter the shell mode:
```bash
<your hepshell alias>
```

# Projects that use hepshell
 - https://github.com/kreczko/l1t_cli
 - https://github.com/BristolTopGroup/NTupleProduction


# Under construction
Refers to future documentation

## installing hepshell
```
pip install hepshell
```

## Using hepshell
```
hep test command
```

## Custom shell
In your project
 - create executable bin/<shell name>
```python
#!/usr/bin/env python
import os
import sys

# adjust paths
current_path = os.path.split(__file__)[0]
path_to_base = os.path.join(current_path, '..')
path_to_base = os.path.abspath(path_to_base)
sys.path.append(path_to_base)

# this is not save in production environemnt
# set HEP_PROJECT_ROOT externally instead
os.environ['HEP_PROJECT_ROOT'] = path_to_base

import hepshell
# specify which command packages to use
hepshell.settings.COMMANDS = [
    'hepshell.commands.core',
    'hepshell.commands.grid',
    'hepshell.commands.exp.cms',
    'hepshell.commands.exp.atlas',
    'hepshell.commands.exp.lz',
    'mypackage.commands.thisone',
]

if len(sys.argv) == 1:
    if not sys.stdout.isatty():
        rc = hepshell.run_command(['help'])
        sys.exit(rc)
    else:
        os.environ['TERM'] = 'vt100'
        name_of_this_script = os.path.basename(sys.argv[0])
        hepshell.run_cli('{0} > '.format(name_of_this_script))
else:
    args = sys.argv[1:]
    rc = hepshell.run_command(args)
    sys.exit(rc)
```
