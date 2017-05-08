
import hepshell.settings as settings


def run_cli(prompt='hep > '):
    if settings.INTERPRETER == settings.INTERPRETERS.LEGACY:
        from hepshell.interpreter_legacy import run_cli
        run_cli(prompt)
    elif settings.INTERPRETER == settings.INTERPRETERS.CLICK_BASED:
        from hepshell.interpreterv2 import run_cli
        run_cli()


def run_command(args):
    if not args:
        return

    if settings.INTERPRETER == settings.INTERPRETERS.LEGACY:
        from hepshell.interpreter_legacy import run_command
        run_command(args)
    elif settings.INTERPRETER == settings.INTERPRETERS.CLICK_BASED:
        from hepshell.interpreterv2 import run_cli
        run_cli(args)
