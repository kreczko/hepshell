# hepshell
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
