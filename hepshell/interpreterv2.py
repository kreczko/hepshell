#!/usr/bin/env python
from __future__ import print_function
import click
import os
from plumbum.cmd import grep



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
    try:
        v1 = grep(['click.command', python_file])
        v2 = grep(['click.command', python_file])
        return r != ''
    except:
        # not a valid command
        return False


class HEPInterpreter(click.MultiCommand):

    def list_commands(self, ctx):
        from . import SETTINGS as s
        rv = []
        for path, _, files in sorted(os.walk(plugin_folder)):
            relative_path = os.path.relpath(path, plugin_folder)
            for f in files:
                if f.endswith('.py'):
                    absolute_path = os.path.join(path, f)
                    if contains_command(absolute_path):
                        c_name = f[:-3]
                        if relative_path == '.':
                            rv.append(c_name)
                        else:
                            c = relative_path.replace('/', ' ')
                            rv.append('{0} {1}'.format(c, c_name))
        return rv

    def get_command(self, ctx, name):
        if name == '__init__':
            return None
        # make a path from the known command
        full_path = name.replace(' ', '/')
        # TODO: replace with logging, DEBUG
        print('Looking for command "{0}"'.format(name))
        ns = {}
        # TODO: look through all plugin folders
        fn = os.path.join(plugin_folder, full_path + '.py')
        # click commands
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        # print('+' * 80)
        # print(name, ns[name.split()[-1]])
        # print('+' * 80)

        ns[name] = ns[name.split()[-1]]
        return ns[name]

    def resolve_command(self, ctx, args):
        '''
            Allow for compound commands just as 'run analysis' by checking
            the command against known commands and adjusting arguments
            accordingly.
        '''
        valid_commads = self.list_commands(ctx)
        passed_cmd = args[0]
        args_start = 1
        n_args = len(args)
        for i in range(n_args):
            tmp_cmd = ' '.join(args[:n_args - i])
            if tmp_cmd in valid_commads:
                passed_cmd = tmp_cmd
                args_start = n_args - i
                break
        new_arguments = [passed_cmd]
        new_arguments.extend(args[args_start:])
        return super(MyCLI, self).resolve_command(ctx, new_arguments)

    # def invoke(self, ctx):
    #     print('>> invoke',ctx.protected_args, ctx.invoked_subcommand)
    #     return super(MyCLI, self).invoke(ctx)
    #
    # def parse_args(self, ctx, args):
    #     print('>> parse', args)
    #     return super(MyCLI, self).parse_args(ctx, args)


@click.group(cls=HEPInterpreter)
@click.pass_context
def run_cli(ctx):
    """ something"""
    print(ctx.invoked_subcommand)
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
