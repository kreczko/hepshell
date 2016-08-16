# hepshell
A Python Shell for High Energy Particle Physics.
hepshell is meant as a starting point for creating your own analysis shell. 
It provides auto-completion (in shell mode), command execution and a few basic
commands such as printing help or creating & checking your grid proxy.


# Setup
<TODO>

A typical HEPSHELL project is expected to have the following minimal folder structure:
 - bin (all scripts/executables)
 - python (all python modules & packages)

In your `{project}/bin` directory add a python script with the following content:

```python
#!/usr/bin/env python

from __future__ import print_function
import os
import readline
import string
import shlex
import sys
import types
import warnings

warnings.filterwarnings("ignore")

current_path = os.path.split(__file__)[0]
# add hepshell python path to PYTHONPATH
path_to_hepshell = os.path.join(current_path, '..', 'python')
sys.path.append(path_to_hepshell)

import hepshell
# TODO: setup external commands

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
    rc = custom_python_shell.run_command(args)
    sys.exit(rc)
```
and make it executable `chmod a+x <the script>`.
The name of the file will be used as the prompt prefix for your custom shell.
Furthermore one should add `{project}/bin/env.sh` which sets up the environment.
At the very least this shell script should define `HEP_PROJECT_ROOT`:
```bash

```
