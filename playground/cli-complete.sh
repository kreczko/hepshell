_cli_completion() {
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \
                   COMP_CWORD=$COMP_CWORD \
                   _CLI_COMPLETE=complete $1 ) )
    return 0
}

complete -F _cli_completion -o default cli;
