Quick note: changes marked with [DEV] are only interested for hepshell developers.

# master

# 0.1.5
 - [DEV] added Command.__extract_additional_parameters
 - parameters of type `--name=value` are now allowed
 - parameters of type `--name` are interpreted as flags (identical to `--name=1`
 
# version 0.1.4
 - fixed typo in `check grid_proxy` command
 - [DEV] added tests
 - [DEV] added Command.__args and basic parsing (just setting the variable)

# version 0.1.3
 - fixed "hidden" commands (issue #1)
 - added CHANGELOG.md

# version 0.1.2
 - [DEV] automatic version lookup for setup.py
 
# version 0.1.1
 - fixed examples mentioning a specific program
 - added miniconda to full env.sh example
 - added unset of temporary variables to minimal env.sh example
 - added CVMFS checks for env.sh examples
 - added `check grid_proxy`
 - added new feature: external commands
 
# version 0.1.0
 - initial port & examples
 