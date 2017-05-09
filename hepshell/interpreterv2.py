#!/usr/bin/env python
from __future__ import print_function
import click
import click_log
import os
from plumbum.cmd import grep
import logging

logger = logging.getLogger(__name__)

# plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')


# def listCommands():
#     for p, d, files in sorted(os.walk(plugin_folder)):
#         for f in files:
#             if f.endswith('.py'):
#                 print(p, f[:-3])
#                 full_path = os.path.join(p, f)
#                 try:
#                     r = grep(['click.command', full_path])
#                     print('+' * 20, 'A valid command')
#                 except:
#                     print('-' * 20, 'Not a valid command')


def contains_command(python_file):
    logger.debug('Checking file {0}'.format(python_file))
    try:
        r = grep(['click.command', python_file])
        return r != ''
    except:
        # not a valid command
        return False


class HEPInterpreter(click.MultiCommand):

    _commands = []

    def list_commands(self, ctx):
        if HEPInterpreter._commands:
            return HEPInterpreter._commands
        from . import SETTINGS as s
        rv = []
        for plugin_folder in s.PLUGINS:
            logger.info('Checking folder {0}'.format(plugin_folder))
            rv.extend(list(self._extract_commands(plugin_folder)))
        HEPInterpreter._commands = rv
        return rv

    def _extract_commands(self, plugin_folder):
        for path, _, files in sorted(os.walk(plugin_folder)):
            relative_path = os.path.relpath(path, plugin_folder)
            for f in files:
                if f.endswith('.py'):
                    absolute_path = os.path.join(path, f)
                    if contains_command(absolute_path):
                        c_name = f[:-3]
                        if relative_path == '.':
                            yield c_name
                        else:
                            c = relative_path.replace('/', ' ')
                            yield '{0} {1}'.format(c, c_name)

    def get_command(self, ctx, name):
        if name == '__init__':
            return None
        from . import SETTINGS as s
        # make a path from the known command
        full_path = name.replace(' ', '/')
        # TODO: replace with logging, DEBUG
        # logger.info('Looking for command "{0}"'.format(name))
        ns = {}
        # TODO: look through all plugin folders
        for plugin_folder in s.PLUGINS:
            fn = os.path.join(plugin_folder, full_path + '.py')
            if not os.path.exists(fn):
                continue
            # click commands
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)

            ns[name] = ns[name.split()[-1]]
            break

        # logger.info(name)
        # logger.info(ns[name].__name__)
        # logger.info(ns.keys())
        if not ns:
            return
        return ns[name]

    def resolve_command(self, ctx, args):
        '''
            Allow for compound commands just as 'run analysis' by checking
            the command against known commands and adjusting arguments
            accordingly.
        '''
        valid_commands = self.list_commands(ctx)
        passed_cmd = None
        args_start = 1
        n_args = len(args)
        for i in range(n_args):
            tmp_cmd = ' '.join(args[:n_args - i])
            if tmp_cmd in valid_commands:
                passed_cmd = tmp_cmd
                args_start = n_args - i
                break
        new_arguments = [passed_cmd]
        new_arguments.extend(args[args_start:])
        return super(HEPInterpreter, self).resolve_command(ctx, new_arguments)

    # def invoke(self, ctx):
    #     print('>> invoke',ctx.protected_args, ctx.invoked_subcommand)
    #     return super(HEPInterpreter, self).invoke(ctx)
    #
    # def parse_args(self, ctx, args):
    #     print('>> parse', args)
    #     return super(HEPInterpreter, self).parse_args(ctx, args)


@click.group(cls=HEPInterpreter)
@click.pass_context
@click_log.simple_verbosity_option()
@click_log.init(__name__)
def run_cli(ctx):
    """ something"""
    pass
    # print(ctx.invoked_subcommand)
    # print(ctx.invoked_subcommand)
    # for k,v in ctx.__dict__.iteritems():
    #     print('{0}: {1}'.format(k, v))
    # c = click.get_current_context()
    # for k,v in c.__dict__.iteritems():
    #     print('{0}: {1}'.format(k, v))


# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet')
# @ntp.command('hello there')
# @click.argument('files',nargs=-1, type=click.Path(exists=True))
# def hello(files):
#     for f in files:
#         click.echo(f)
#
# @ntp.command()
# def dropdb():
#     click.echo('Dropped the database')
