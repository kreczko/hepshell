```bash
export PATH=$PWD/playground:$PATH
eval "$(_CLI_COMPLETE=source cli)"
# or
_CLI_COMPLETE=source cli > cli-complete.sh
. cli-complete.sh
